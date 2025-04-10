from dataclasses import dataclass
from typing import Any
from telegram_framework.messages.errors import MessageNotInChatError
from telegram_framework.messages.text_message import MessageDefault
from telegram_framework.messages.core import is_chat_message
from .reply_base import ReplyBase



@dataclass(frozen=True)
class Reply(MessageDefault, ReplyBase):

    def __eq__(self, other):
        return (
                self.text == other.text
                and self.sender == other.sender
                and self.message == other.message
                )



def create_reply(message, text:str, sender: Any) -> Reply:
    if not is_chat_message(message):
        raise MessageNotInChatError(message)

    return Reply(
        text=text,
        sender=sender,
        message=message,
        chat=message.chat,
    )
