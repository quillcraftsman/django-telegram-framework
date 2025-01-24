from dataclasses import dataclass
from .chat_message_base import ChatMessageBase
from .message_default import MessageDefault
from .message import Message

@dataclass(frozen=True)
class ChatMessage(MessageDefault, ChatMessageBase):
    pass


def create_chat_message(message: Message, chat):
    return ChatMessage(
        text=message.text,
        sender=message.sender,
        chat=chat,
    )