from typing import Callable
from telebot import TeleBot
from . import adapters


def register_command_handler(bot: TeleBot, handler: Callable, name: str, filter_function=None):
    handler = adapters.prepare_handler(handler, bot)
    bot.register_message_handler(handler, commands=[name], func=filter_function)
    return bot


def register_next_step_handler(bot: TeleBot, chat, handler: Callable):
    handler = adapters.prepare_handler(handler, bot)
    bot.register_next_step_handler_by_chat_id(chat.id, handler)
    return chat


def register_message_handler(
        bot: TeleBot, handler: Callable,
        filter_function: Callable = lambda message: True
    ):
    handler = adapters.prepare_handler(handler, bot)
    bot.register_message_handler(handler, func=filter_function)
    return bot


def register_text_handler(bot: TeleBot, handler: Callable, text: str):
    return register_message_handler(bot, handler, lambda message: message.text == text)


def register_call_handler(bot: TeleBot, handler: Callable, call_data:str, filter_function=None):
    filter_function = filter_function \
        if filter_function \
        else lambda call_obj: call_obj.data == call_data
    handler = adapters.prepare_call_handler(handler, bot)
    bot.register_callback_query_handler(
        handler,
        func=filter_function,
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
