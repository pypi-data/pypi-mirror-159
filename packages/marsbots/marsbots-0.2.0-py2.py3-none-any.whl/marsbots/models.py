from dataclasses import dataclass
from typing import List


@dataclass
class MarsBotSettings:
    name: str
    token_env: str
    command_prefix: str
    intents: List[str]


@dataclass
class ChatMessage:
    content: str
    sender: str
    deliniator_left: str = "**["
    deliniator_right: str = "]**:"

    def __str__(self) -> str:
        return (
            f"{self.deliniator_left}{self.sender}{self.deliniator_right} {self.content}"
        )
