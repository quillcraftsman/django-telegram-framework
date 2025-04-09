from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class MessageToSend:
    sender: Any


@dataclass(frozen=True)
class MessageBase(MessageToSend):
    text: str
    # sender: Any
