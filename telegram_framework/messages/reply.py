from dataclasses import dataclass
from typing import Any
from .errors import MessageNotInChatError
from .message_default import MessageDefault
from .reply_base import ReplyBase
from .message import Message


@dataclass(frozen=True)
class Reply(MessageDefault, ReplyBase):

    def __eq__(self, other):
        return (
                self.text == other.text
                and self.sender == other.sender
                and self.message == other.message
                )



def create_reply(message: Message, text:str, sender: Any) -> Reply:
    if not message.chat:
        raise MessageNotInChatError(message)
    return Reply(text, sender, message, chat=message.chat)
