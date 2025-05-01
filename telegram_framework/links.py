from typing import Callable
import importlib
from telegram_framework import bots
from .commands import description


def on_command(handler: Callable, name: str, description_text=None):

    if description_text:
        handler = description(description_text)(handler)

    def command_handler(bot):

        return bots.register_command_handler(bot, handler, name)

    return command_handler


def on_message(handler: Callable, filter_function: Callable = lambda message: True):

    def message_handler(bot):
        return bots.register_message_handler(bot, handler, filter_function)

    return message_handler


def on_text(handler: Callable, text: str):

    def text_handler(bot):
        return bots.register_text_handler(bot, handler, text)

    return text_handler


def on_call(handler, call_data):

    def call_handler(bot):
        return bots.register_call_handler(bot, handler, call_data)

    return call_handler


def add_links(bot, links):
    for link in links:
        bot = link(bot)

    return bot


def get_root_links(module_name):
    links_module = importlib.import_module(module_name)
    return links_module.bot_links


def include(links: list, module_name) -> list:
    additional_links = get_root_links(module_name)
    return links + additional_links


def include_all(links: list, modules_list: list) -> list:
    for module in modules_list:
        links = include(links, module)
    return links
