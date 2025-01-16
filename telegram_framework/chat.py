from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Chat:
    id: int = 0
    messages: list = field(default_factory=list)
    bots: list = field(default_factory=list)


def _update_chat(chat: Chat, **kwargs):
    chat_dict = chat.__dict__.copy()
    for k,v in kwargs.items():
        chat_dict[k] = v
    return Chat(**chat_dict)


def add_bot(chat: Chat, bot: Any) -> Chat:
    _update_chat(chat)
    new_bots = chat.bots + [bot]
    return _update_chat(chat, bots=new_bots)


def add_message(chat: Chat, message: Any) -> Chat:
    new_messages = chat.messages + [message]
    return _update_chat(chat, messages=new_messages)


def get_last_message(chat: Chat) -> Any:
    if not chat.messages:
        return None
    return chat.messages[-1]
