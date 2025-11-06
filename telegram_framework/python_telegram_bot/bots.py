from typing import Callable
from telegram.ext import Updater, CommandHandler
from . import adapters

def get_bot(token):
    updater = Updater(token, use_context=True)
    return updater


def start(bot: Updater):
    bot.start_polling()
    bot.idle()


def register_command_handler(bot: Updater, handler: Callable, name: str, filter_function=None):  # pylint:disable=(unused-argument)
    dp = bot.dispatcher
    handler = adapters.prepare_handler(handler, bot)
    dp.add_handler(CommandHandler(name, handler))
    return bot


def register_text_handler(bot: Updater, handler: Callable, text: str):  # pylint:disable=(unused-argument)
    return bot


def register_call_handler(bot: Updater, handler: Callable, call_data:str, filter_function=None):  # pylint:disable=(unused-argument)
    return bot


def register_message_handler(
        bot: Updater, handler: Callable,
        filter_function: Callable = lambda message: True
    ):  # pylint:disable=(unused-argument)
    return bot
