import logging
import subprocess
import sys
from typing import List

from ..model.command import Command


def run_command(cmd: List[Command]) -> subprocess.CompletedProcess:
    logger = logging.getLogger(__name__)
    logger.debug(
        f"""Running command:
  cmd   = {cmd.command}
  cwd   = {cmd.cwd}
  shell = {cmd.shell}
    """
    )
    ret = subprocess.run(
        cmd.command,
        check=True,
        cwd=cmd.cwd,
        shell=cmd.shell,
        stdout=sys.stdout,
        stderr=sys.stderr,
    )
    logger.info(
        f"""Ran command successfully:
  cmd   = {cmd.command}
  cwd   = {cmd.cwd}
  shell = {cmd.shell}
  rc    = {ret.returncode}
    """
    )
    return ret
