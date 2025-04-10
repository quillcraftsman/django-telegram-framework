from dataclasses import dataclass
from typing import Any
from telegram_framework.messages.text_message import MessageBase

@dataclass(frozen=True)
class ChatMessageBase(MessageBase):
    chat: Any


def is_chat_message(message):
    return hasattr(message, 'chat')
