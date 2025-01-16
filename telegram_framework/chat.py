from dataclasses import dataclass, field
from typing import Any
from telegram_framework.functions import update


@dataclass(frozen=True)
class Chat:
    id: int = 0
    messages: list = field(default_factory=list)
    bots: list = field(default_factory=list)

    def __eq__(self, other):
        return self.id == other.id


def add_bot(chat: Chat, bot: Any) -> Chat:
    new_bots = chat.bots + [bot]
    return update(chat, bots=new_bots)


def add_message(chat: Chat, message: Any) -> Chat:
    chat_message = update(message, chat=chat)
    new_messages = chat.messages + [chat_message]
    return update(chat, messages=new_messages)


def get_last_message(chat: Chat) -> Any:
    if not chat.messages:
        return None
    return chat.messages[-1]
