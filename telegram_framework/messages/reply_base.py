from dataclasses import dataclass
from .message_base import MessageBase
from .message import Message

@dataclass(frozen=True)
class ReplyBase(MessageBase):
    message: Message
