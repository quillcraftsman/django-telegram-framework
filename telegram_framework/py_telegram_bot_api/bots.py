import functools
from typing import Callable
from telebot import TeleBot


def prepare_handler(handler_function, bot):

    @functools.wraps(handler_function)
    def inner(*args, **kwargs):
        return handler_function(bot, *args, **kwargs)

    return inner


def register_command_handler(bot: TeleBot, handler: Callable, name: str):
    handler = prepare_handler(handler, bot)
    bot.register_message_handler(handler, commands=[name])
    return bot


def register_message_handler(bot: TeleBot, handler: Callable):
    handler = prepare_handler(handler, bot)
    bot.register_message_handler(handler, func=lambda m: True)
    return bot


def register_call_handler(bot: TeleBot, handler: Callable, call_data):
    handler = prepare_handler(handler, bot)
    bot.register_callback_query_handler(
        handler,
        func=lambda call_obj: call_obj.data == call_data,
    )
    return bot


def get_bot(token):
    return TeleBot(token=token)


def start(bot: TeleBot):
    bot.infinity_polling()


def handle_message(bot, message):  # pylint: disable=unused-argument
    return message.chat


def find_handler(bot: TeleBot, message):  # pylint: disable=unused-argument
    return None


def get_commands_list(bot: TeleBot):
    handlers = bot.message_handlers
    commands = []
    for handler in handlers:
        handler_filters = handler['filters']
        if 'commands' in handler_filters:
            tele_bot_commands = handler_filters['commands']
            for command in tele_bot_commands:
                commands.append((command, handler['function']))
    return commands
