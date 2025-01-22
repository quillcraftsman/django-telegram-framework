from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class MessageBase:
    text: str
    sender: Any
