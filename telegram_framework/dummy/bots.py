from dataclasses import dataclass, field
from typing import List, Dict, Callable
from telegram_framework import functions, handlers
from telegram_framework.messages import Message, Image, Call


@dataclass(frozen=True)
class DummyBot:
    token: str
    command_handlers: Dict[str, handlers.Handler] = field(default_factory=dict)
    message_handlers: List[handlers.Handler] = field(default_factory=list)
    call_handlers: Dict[str, handlers.Handler] = field(default_factory=dict)

    @property
    def id(self):
        return self.token


def register_command_handler(bot: DummyBot, handler: Callable, name: str, filter_function=None):
    handler = handlers.create_handler(handler, filter_function=filter_function)
    command_handlers = bot.command_handlers | {name: handler}
    return functions.update(bot, command_handlers=command_handlers)


def register_message_handler(
        bot: DummyBot,
        handler: Callable,
        filter_function: Callable = lambda message: True
    ):
    handler = handlers.create_handler(handler, filter_function)
    message_handlers = bot.message_handlers + [handler]
    return functions.update(bot, message_handlers=message_handlers)


def register_text_handler(bot: DummyBot, handler: Callable, text: str):
    return register_message_handler(bot, handler, lambda message: message.text == text)


def register_call_handler(
        bot: DummyBot,
        handler: Callable,
        call_data: str,
        filter_function:
        Callable=None
    ):
    handler = handlers.create_handler(handler, filter_function)
    call_handlers = bot.call_handlers | {call_data: handler}
    return functions.update(bot, call_handlers=call_handlers)


def find_handler(bot: DummyBot, message):
    if isinstance(message, Call):
        # return bot.call_handlers.get(message.data, None)
        for _, handler in bot.call_handlers.items():
            filter_function = handler.filter
            if filter_function(message):
                return handler
    text = ''
    if isinstance(message, Message):
        text = message.text
    elif isinstance(message, Image) and message.caption is not None:
        text = message.caption.text
    if text.startswith('/'):
        # this is command
        # command_name = text.replace('/', '')
        # return bot.command_handlers.get(command_name, None)
        for _, handler in bot.command_handlers.items():
            filter_function = handler.filter
            if filter_function(message):
                return handler
    # this is message
    for handler in bot.message_handlers:
        filter_function = handler.filter
        if filter_function(message):
            return handler
    return None


def get_bot(token):
    return DummyBot(token=token)


def start(bot: DummyBot):  # pylint: disable=unused-argument
    pass


def handle_message(bot, message):
    handler = find_handler(bot, message)
    if not handler:
        return message.chat
    return handler.function(bot, message)


def get_commands_list(bot: DummyBot):
    # commands = list(bot.command_handlers.items())
    commands = [(name, handler.function) for name, handler in bot.command_handlers.items()]
    return commands
