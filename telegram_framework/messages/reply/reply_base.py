from dataclasses import dataclass
from telegram_framework.messages.text_message import MessageBase


@dataclass(frozen=True)
class ReplyBase(MessageBase):
    message: MessageBase
