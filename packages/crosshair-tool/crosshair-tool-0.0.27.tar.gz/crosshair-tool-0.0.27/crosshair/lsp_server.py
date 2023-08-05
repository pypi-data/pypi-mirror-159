import pathlib
import re
import sys
import time
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from threading import Thread
from typing import Any, Counter, Dict, List, Optional
from urllib.parse import urlparse

import pygls.lsp.methods as lsmethods
from pygls.lsp.types import (
    Diagnostic,
    DiagnosticSeverity,
    DidChangeTextDocumentParams,
    DidCloseTextDocumentParams,
    DidOpenTextDocumentParams,
    Position,
    Range,
)
from pygls.server import LanguageServer

from crosshair.options import AnalysisOptionSet
from crosshair.statespace import AnalysisMessage, MessageType
from crosshair.watcher import Watcher


class CrossHairLanguageServer(LanguageServer):
    def __init__(self, options: AnalysisOptionSet):
        self.options = options
        super().__init__()

    CMD_REGISTER_COMPLETIONS = "registerCompletions"
    CMD_UNREGISTER_COMPLETIONS = "unregisterCompletions"


def get_diagnostic(message: AnalysisMessage, doclines: List[str]) -> Diagnostic:
    line = message.line - 1
    col = endcol = message.column
    if col == 0:
        if line < len(doclines):
            line_text = doclines[line]
            match = re.compile(r"^\s*(.*?)\s*$").fullmatch(line_text)
            if match:
                col, endcol = match.start(1), match.end(1)
    if message.state < MessageType.PRE_UNSAT:
        severity = DiagnosticSeverity.Information
    elif message.state == MessageType.PRE_UNSAT:
        severity = DiagnosticSeverity.Warning
    else:
        severity = DiagnosticSeverity.Error
    return Diagnostic(
        range=Range(
            start=Position(line=line, character=col),
            end=Position(line=line, character=endcol),
        ),
        severity=severity,
        message=message.message,
        source="CrossHair",
    )


def publish_messages(
    messages: Dict[str, Optional[Dict[int, AnalysisMessage]]],
    server: CrossHairLanguageServer,
):
    for uri, file_messages in list(messages.items()):
        doc = server.workspace.documents.get(uri, None)
        if file_messages is None:
            # closed/editing, and client already notified as empty
            continue
        diagnostics = []
        for message in file_messages.values():
            if message.state < MessageType.PRE_UNSAT:
                continue
            # TODO: consider server.show_message_log()ing the long description
            diagnostics.append(get_diagnostic(message, doc.lines if doc else ()))
        server.publish_diagnostics(uri, diagnostics)
        if not diagnostics:
            # After we publish an empty set, it's safe to forget about the file:
            del messages[uri]


@dataclass
class LocalState:
    watcher: Watcher
    server: CrossHairLanguageServer
    loop: Optional[Thread] = None
    active_messages: Dict[str, Optional[Dict[int, AnalysisMessage]]] = field(
        default_factory=lambda: defaultdict(dict)
    )
    should_shutdown: bool = False

    def start_loop_thread(self):
        self.loop = Thread(target=self.run_watch_loop)
        self.loop.start()

    def run_watch_loop(
        self,
        max_watch_iterations: int = sys.maxsize,
    ) -> None:
        watcher = self.watcher
        server = self.server
        active_messages = self.active_messages
        restart = True
        stats: Counter[str] = Counter()
        for _ in range(max_watch_iterations):
            if self.should_shutdown:
                return
            if restart:
                numfiles = len(watcher._modtimes)
                server.show_message_log(
                    f"Scanning {numfiles} file(s) for properties to check."
                )
                max_condition_timeout = 0.5
                restart = False
                stats = Counter()
                for k, v in list(active_messages.items()):
                    active_messages[k] = None if v is None else {}
            else:
                time.sleep(0.25)
                max_condition_timeout = min(
                    sys.float_info.max, 2 * max_condition_timeout
                )
            for curstats, messages in watcher.run_iteration(max_condition_timeout):
                stats.update(curstats)
                for message in messages:
                    filename, line = (message.filename, message.line)
                    file_messages = active_messages[Path(filename).as_uri()]
                    if file_messages is not None and (
                        line not in file_messages
                        or file_messages[line].state < message.state
                    ):
                        file_messages[line] = message
            numpaths = stats["num_paths"]
            if self.should_shutdown:
                return
            if numpaths > 0:
                status = f"Analyzed {numpaths} paths in {len(watcher._modtimes)} files."
                server.show_message_log(status)
            publish_messages(active_messages, server)
            if watcher._change_flag:
                watcher._change_flag = False
                restart = True


_LS: Optional[LocalState] = None


def getlocalstate(server: CrossHairLanguageServer) -> LocalState:
    global _LS
    if _LS is None:
        watcher = Watcher([], server.options)
        watcher.startpool()
        _LS = LocalState(watcher, server)
        _LS.start_loop_thread()
    else:
        _LS.server = server
    return _LS


def update_paths(server: CrossHairLanguageServer):
    paths = []
    for uri, doc in server.workspace.documents.items():
        if not doc.filename.endswith(".py"):
            continue
        parsed = urlparse(uri)
        if parsed.netloc != "":
            continue
        paths.append(pathlib.Path(parsed.path))
    watcher = getlocalstate(server).watcher
    watcher.update_paths(paths)


def create_lsp_server(options: AnalysisOptionSet) -> CrossHairLanguageServer:

    crosshair_lsp_server = CrossHairLanguageServer(options)

    @crosshair_lsp_server.feature(lsmethods.TEXT_DOCUMENT_DID_CHANGE)
    def did_change(
        server: CrossHairLanguageServer, params: DidChangeTextDocumentParams
    ):
        uri = params.text_document.uri
        getlocalstate(server).active_messages[uri] = None
        server.publish_diagnostics(uri, [])

    @crosshair_lsp_server.feature(lsmethods.TEXT_DOCUMENT_DID_CLOSE)
    def did_close(server: CrossHairLanguageServer, params: DidCloseTextDocumentParams):
        uri = params.text_document.uri
        getlocalstate(server).active_messages[uri] = None
        server.publish_diagnostics(uri, [])
        update_paths(server)

    @crosshair_lsp_server.feature(lsmethods.TEXT_DOCUMENT_DID_OPEN)
    async def did_open(
        server: CrossHairLanguageServer, params: DidOpenTextDocumentParams
    ):
        uri = params.text_document.uri
        getlocalstate(server).active_messages[uri] = {}
        update_paths(server)

    @crosshair_lsp_server.feature(lsmethods.TEXT_DOCUMENT_DID_SAVE)
    async def did_save(
        server: CrossHairLanguageServer, params: DidOpenTextDocumentParams
    ):
        uri = params.text_document.uri
        update_paths(server)
        getlocalstate(server).active_messages[uri] = {}
        server.publish_diagnostics(uri, [])

    @crosshair_lsp_server.feature(lsmethods.SHUTDOWN)
    async def did_shutdown(
        server: CrossHairLanguageServer,
        params: Any,
    ):
        getlocalstate(server).should_shutdown = True

    return crosshair_lsp_server
