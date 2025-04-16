from typing import Callable
import importlib
from telegram_framework import bots


def on_command(handler: Callable, name: str):

    def command_handler(bot):
        return bots.register_command_handler(bot, handler, name)

    return command_handler


def on_message(handler: Callable):

    def message_handler(bot):
        return bots.register_message_handler(bot, handler)

    return message_handler


# def on_call(handler, call_data):
#
#     def call_handler(bot):
#         return register_call_handler(bot, handler, call_data)
#
#     return call_handler


def add_links(bot, links):
    for link in links:
        bot = link(bot)

    return bot


def get_root_links(module_name):
    links_module = importlib.import_module(module_name)
    return links_module.bot_links
