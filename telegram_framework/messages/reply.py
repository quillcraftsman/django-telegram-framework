from dataclasses import dataclass
from typing import Any
from .errors import MessageNotInChatError
from .message_default import MessageDefault
from .reply_base import ReplyBase
from .chat_message_base import ChatMessageBase


@dataclass(frozen=True)
class Reply(MessageDefault, ReplyBase):

    def __eq__(self, other):
        return (
                self.text == other.text
                and self.sender == other.sender
                and self.message == other.message
                )



def create_reply(message: ChatMessageBase, text:str, sender: Any) -> Reply:
    if not isinstance(message, ChatMessageBase):
        raise MessageNotInChatError(message)

    return Reply(
        text=text,
        sender=sender,
        message=message,
        chat=message.chat,
    )