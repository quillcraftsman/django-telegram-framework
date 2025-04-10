from dataclasses import dataclass, field
from typing import List, Dict, Callable
from telegram_framework import functions
from telegram_framework.messages import Message, Image


@dataclass(frozen=True)
class DummyBot:
    token: str
    command_handlers: Dict[str, Callable] = field(default_factory=dict)
    message_handlers: List[Callable] = field(default_factory=list)
    call_handlers: Dict[str, Callable] = field(default_factory=dict)


def register_command_handler(bot: DummyBot, handler: Callable, name: str):
    command_handlers = bot.command_handlers | {name: handler}
    return functions.update(bot, command_handlers=command_handlers)


def register_message_handler(bot: DummyBot, handler: Callable):
    message_handlers = bot.message_handlers + [handler]
    return functions.update(bot, message_handlers=message_handlers)


def register_call_handler(bot: DummyBot, handler: Callable, call_data):
    call_handlers = bot.call_handlers | {call_data: handler}
    return functions.update(bot, call_handlers=call_handlers)


def find_handler(bot: DummyBot, message):
    text = ''
    if isinstance(message, Message):
        text = message.text
    elif isinstance(message, Image) and message.caption is not None:
        text = message.caption.text
    if text.startswith('/'):
        # this is command
        command_name = text.replace('/', '')
        return bot.command_handlers.get(command_name, None)
    # this is message
    return bot.message_handlers[0] if bot.message_handlers else None


def get_bot(token):
    return DummyBot(token=token)


def start(bot: DummyBot):  # pylint: disable=unused-argument
    pass


def handle_message(bot, message):
    handler = find_handler(bot, message)
    if not handler:
        return message.chat
    return handler(bot, message)
