from dataclasses import dataclass, field
from typing import Any
from telegram_framework.functions import update
from telegram_framework import bots
from telegram_framework import messages, keyboards


@dataclass(frozen=True)
class Chat:
    id: int = 0
    messages: list = field(default_factory=list)
    bots: list = field(default_factory=list)
    keyboard: Any = None

    def __eq__(self, other):
        return self.id == other.id


def add_keyboard(chat:Chat, keyboard: Any):
    return update(chat, keyboard=keyboard)


def add_bot(chat: Chat, bot: Any) -> Chat:
    new_bots = chat.bots + [bot]
    return update(chat, bots=new_bots)


def add_message(chat: Chat, message: Any) -> Chat:
    keyboard = message.keyboard
    if message.keyboard and isinstance(keyboard, keyboards.reply.Keyboard):
        chat = add_keyboard(chat, message.keyboard)
    chat_message = message
    if not messages.is_chat_message(chat_message):
        chat_message = messages.create_chat_message(chat_message, chat)
    new_messages = chat.messages + [chat_message]
    chat = update(chat, messages=new_messages)
    for bot in chat.bots:
        last_message = get_last_message(chat)
        if last_message:
            if last_message.sender != bot:
                chat = bots.handle_message(bot, last_message)
    return chat


def get_last_message(chat: Chat) -> Any:
    if not chat.messages:
        return None
    last_message = chat.messages[-1]
    last_chat_message = update(last_message, chat=chat)
    return last_chat_message
    #return last_message

# def get_messages(chat: Chat):
#     chat_messages = [update(message, chat=chat) for message in chat.messages]
#     return chat_messages
