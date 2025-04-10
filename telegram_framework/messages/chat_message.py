from dataclasses import dataclass
from telegram_framework.messages.text_message import MessageDefault, Message
from .chat_message_base import ChatMessageBase



@dataclass(frozen=True)
class ChatMessage(MessageDefault, ChatMessageBase):
    pass


def create_chat_message(message: Message, chat):
    return ChatMessage(
        text=message.text,
        sender=message.sender,
        chat=chat,
    )
