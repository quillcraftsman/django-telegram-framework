from dataclasses import dataclass
from telegram_framework.messages.chat_message_base import ChatMessageBase


@dataclass(frozen=True)
class ReplyBase(ChatMessageBase):
    message: ChatMessageBase
