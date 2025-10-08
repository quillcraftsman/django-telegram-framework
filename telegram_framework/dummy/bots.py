from dataclasses import dataclass, field, replace
from typing import List, Dict, Callable
from telegram_framework import handlers
from telegram_framework.messages import Message, Image, Call
from telegram_framework.user import UserData


@dataclass(frozen=True)
class DummyBot:
    token: str
    user_data: UserData
    command_handlers: Dict[str, handlers.Handler] = field(default_factory=dict)
    message_handlers: List[handlers.Handler] = field(default_factory=list)
    call_handlers: Dict[str, handlers.Handler] = field(default_factory=dict)
    next_step_handler: Callable = None


    @property
    def id(self):
        return self.token

    def __eq__(self, other):
        return self.id == other.id


def register_command_handler(bot: DummyBot, handler: Callable, name: str, filter_function=None):
    handler = handlers.create_handler(handler, filter_function=filter_function)
    command_handlers = bot.command_handlers | {name: handler}
    return replace(bot, command_handlers=command_handlers)


def register_message_handler(
        bot: DummyBot,
        handler: Callable,
        filter_function: Callable = lambda message: True
    ):
    handler = handlers.create_handler(handler, filter_function)
    message_handlers = bot.message_handlers + [handler]
    return replace(bot, message_handlers=message_handlers)


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
    return replace(bot, call_handlers=call_handlers)


def update_bot(chat, bot):
    old_bots = chat.bots
    new_bots = []
    for current_bot in old_bots:
        if current_bot.token == bot.token:
            new_bots.append(bot)
        else:
            new_bots.append(current_bot)
    return replace(chat, bots=new_bots)



def register_next_step_handler(
        bot: DummyBot,
        chat,
        handler: Callable
):
    handler = handlers.create_handler(handler)
    bot = replace(bot, next_step_handler=handler)
    chat = update_bot(chat, bot)
    return chat


def find_handler(bot: DummyBot, message):
    if bot.next_step_handler:
        return bot.next_step_handler
    if isinstance(message, Call):
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


def get_bot(token, user_data=None):
    user_data = user_data if user_data else UserData(id=token)
    return DummyBot(token=token, user_data=user_data)


def start(bot: DummyBot):  # pylint: disable=unused-argument
    pass


def handle_message(bot, message):
    handler = find_handler(bot, message)
    if not handler:
        return message.chat
    # remove next step handler
    if handler == bot.next_step_handler:
        # Какая-то дичь. Надо придумать что делать с комбинацией чата и бота
        bot = replace(bot, next_step_handler=None)
        chat = message.chat
        chat = update_bot(chat, bot)
        message = replace(message, chat=chat)
    return handler.function(bot, message)


def get_commands_list(bot: DummyBot):
    commands = [(name, handler.function) for name, handler in bot.command_handlers.items()]
    return commands
