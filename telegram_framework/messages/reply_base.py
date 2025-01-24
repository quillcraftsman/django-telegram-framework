from dataclasses import dataclass
from .chat_message_base import ChatMessageBase


@dataclass(frozen=True)
class ReplyBase(ChatMessageBase):
    message: ChatMessageBase
