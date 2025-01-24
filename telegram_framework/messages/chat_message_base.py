from dataclasses import dataclass
from typing import Any
from .message_base import MessageBase

@dataclass(frozen=True)
class ChatMessageBase(MessageBase):
    chat: Any
