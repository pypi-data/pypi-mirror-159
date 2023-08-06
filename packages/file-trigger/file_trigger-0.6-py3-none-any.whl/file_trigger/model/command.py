from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Command:
    name: str
    command: List[str]
    cwd: Optional[str]
    shell: bool = False

    def __str__(self) -> str:
        command_tokens = [repr(t) for t in self.command]
        cwd_str = "(parent)" if self.cwd is None else self.cwd
        return "\n".join(
            [
                f"{self.name}:",
                "-" * (len(self.name) + 1),
                f"  command = [ {', '.join(command_tokens)} ]",
                f"  cwd = {cwd_str}",
                f"  shell = {self.shell}",
            ]
        )
