from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
from typing import Iterable, List, Tuple

from ..adapter import subprocess_
from ..model.command import Command


class ExecutionErrors(Exception):
    def __init__(self, errors: Iterable[Tuple[str, Command, Exception]]):
        self.errors = errors

    def __str__(self) -> str:
        return "\n".join(
            [
                f"Execution error{'s' if len(self.errors) > 1 else ''} (check logs for details):"
            ]
            + [
                f"  {i+1}. {handler}: Error running command {cmd.name}:\n{e}"
                for (i, (handler, cmd, e)) in enumerate(self.errors)
            ]
        )


class CommandExecutor:
    def __init__(self, **kwargs):
        self._executor = ThreadPoolExecutor(**kwargs)
        self._errors: List[Tuple[str, Command, Exception]] = []
        self.logger = logging.getLogger(__name__)

    def submit_commands(self, cmds: Iterable[Tuple[str, Command]], *, prefix: str = ""):
        f_map = {
            self._executor.submit(run_command, cmd, handler, prefix=prefix): (
                handler,
                cmd,
            )
            for (handler, cmd) in cmds
        }
        for f in as_completed(f_map):
            handler, cmd = f_map[f]
            try:
                f.result()
            except Exception as e:
                self.logger.error(
                    f"{prefix}: {handler}: Error running command {cmd.name}"
                )
                self.logger.exception(e)
                self._errors.append((handler, cmd, e))

    def shutdown(self):
        self.logger.debug("Shutting down executor")
        self._executor.shutdown(wait=True)
        if len(self._errors) > 0:
            self.logger.debug(f"Shut down executor: {len(self._errors)} errors raised")
            raise ExecutionErrors(self._errors)
        else:
            self.logger.info("Shut down executor.")


def run_command(cmd: Command, handler: str, *, prefix: str):
    logger = logging.getLogger(__name__)
    logger.debug(f"{prefix}: {handler}: Running command {cmd.name}")
    subprocess_.run_command(cmd)
    logger.info(f"{prefix}: {handler}: Ran command {cmd.name}")
