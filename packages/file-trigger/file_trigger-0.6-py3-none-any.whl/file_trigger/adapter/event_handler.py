import logging
import os.path
from time import time
from typing import Any, Optional, Dict, Tuple, List

from watchdog.events import (
    FileSystemEvent,
    PatternMatchingEventHandler,
)  # type: ignore

from ..adapter.executor import CommandExecutor
from ..adapter.filesys import Matcher
from ..model.command import Command
from ..model.config import Config, HandlerConfig
from ..util import datetime_
from ..util.watchdog import event_type_and_file_names_from_event


class EventHandler(PatternMatchingEventHandler):
    def __init__(self, config: Config, executor: CommandExecutor):
        super().__init__(
            patterns=config.patterns,
            ignore_patterns=config.ignore_patterns,
            ignore_directories=config.ignore_directories,
        )
        self.last_event: Optional[FileSystemEvent] = None
        self.last_timestamp: Optional[float] = None
        self.config: Config = config
        self._executor: CommandExecutor = executor

    def on_any_event(self, event: FileSystemEvent):
        ts = time()
        logger = logging.getLogger(__name__)
        logger.debug(f"Received event: {event}")
        if self.ignore_event(event=event, timestamp=ts):
            logger.debug(f"Ignored event as duplicate: {event}")
        else:
            self.handle_event_on_thread(event=event, timestamp=ts)
        self.last_event = event
        self.last_timestamp = ts

    def ignore_event(self, event: FileSystemEvent, timestamp: float) -> bool:
        """filter out duplicate-ish events thrown up by Windows"""
        if self.last_timestamp is None or self.last_event is None:
            return False

        if (
            event == self.last_event
            and event.src_path == self.last_event.src_path
            and (timestamp - self.last_timestamp < 1)
        ):
            return True

        return False

    def handle_event_on_thread(self, event: FileSystemEvent, timestamp: float):
        prefix = f"{event.event_type.upper()} {event.src_path}"
        self._executor.submit_commands(
            commands_triggered_by_handlers(
                self.config, event=event, prefix=prefix, timestamp=timestamp
            ),
            prefix=prefix,
        )


def commands_triggered_by_handlers(
    config: Config, *, event: FileSystemEvent, prefix: str, timestamp: float
) -> List[Tuple[str, Command]]:
    logger = logging.getLogger(__name__)

    cmds: List[Tuple[str, Command]] = []
    for h in config.handlers:
        matched_cmds = render_commands(
            h,
            event=event,
            root_dir=config.root_dir,
            prefix=prefix,
            timestamp=timestamp,
        )
        n_cmds = len(matched_cmds)
        if n_cmds == 0:
            logger.debug(f"{prefix}: Did not match handler {h.name}")
        else:
            logger.info(
                f"{prefix}: Handled by {h.name}: "
                f"triggering {n_cmds} command{'s' if n_cmds>1 else ''}"
            )
        for cmd in matched_cmds:
            cmds.append((h.name, cmd))
    return cmds


def render_commands(
    handler: HandlerConfig,
    *,
    event: FileSystemEvent,
    root_dir: str,
    prefix: str,
    timestamp: float,
) -> List[Command]:
    logger = logging.getLogger(__name__)
    event_type, file, _ = event_type_and_file_names_from_event(event)

    empty_commands: List[Command] = []
    if handler.events is not None and event_type not in handler.events:
        logger.debug(f"{prefix}: {handler.name}: ignored {event_type}")
        return empty_commands

    try:
        rel_file = os.path.relpath(file, root_dir)
    except ValueError as e:
        logger.debug(f"{prefix}: ignored because of error comparing paths: {e}")

    captures = Matcher(handler.template).match(rel_file)
    if captures is None:
        logger.debug(
            f"{prefix}: {handler.name}: ignored because file didn't match template"
        )
        return empty_commands

    data: Dict[str, Any] = {}
    for k in captures:
        data[k] = captures[k]
    data["ROOT_DIR"] = root_dir
    data["TIMESTAMP_POSIX"] = timestamp
    data["TIMESTAMP"] = datetime_.from_posix(timestamp)
    data["TIMESTAMP_UTC"] = datetime_.utc_from_posix(timestamp)
    data["FILE_PATH"] = file
    data["RELATIVE_FILE_PATH"] = rel_file
    data["DIR_PATH"] = os.path.dirname(file)
    data["RELATIVE_DIR_PATH"] = os.path.dirname(rel_file)
    data["FILE_NAME"] = os.path.basename(file)
    data["FILE_EXT"] = os.path.splitext(file)[1][1:]

    try:
        return [
            Command(
                name=c.name,
                command=[token.format(**data) for token in c.command],
                cwd=None if c.cwd is None else c.cwd.format(**data),
                shell=c.shell,
            )
            for c in handler.commands
        ]

    except KeyError as e:
        raise ValueError(f"Unknown variable in command: {e}")
