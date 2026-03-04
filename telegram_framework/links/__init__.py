from typing import Callable
import importlib
from telegram_framework import bots
from telegram_framework.commands import description
from . import params


def on_command(handler: Callable, name: str, description_text=None, params_pattern=None):

    if description_text:
        handler = description(description_text)(handler)

    params_pattern = params_pattern if params_pattern else name
    handler = params.prepare_handler(handler, params_pattern, 'command')
    filter_function = params.get_filter_function(params_pattern, 'command')

    def command_handler(bot):

        return bots.register_command_handler(bot, handler, name, filter_function)

    return command_handler


def on_message(handler: Callable, filter_function: Callable = lambda message: True):

    def message_handler(bot):
        return bots.register_message_handler(bot, handler, filter_function)

    return message_handler


def on_text(handler: Callable, text: str):

    def text_handler(bot):
        return bots.register_text_handler(bot, handler, text)

    return text_handler


def on_call(handler, call_data, params_pattern=None):

    params_pattern = params_pattern if params_pattern else call_data
    handler = params.prepare_handler(handler, params_pattern, 'call')
    filter_function = params.get_filter_function(params_pattern, 'call')

    def call_handler(bot):
        return bots.register_call_handler(
            bot,
            handler,
            call_data,
            filter_function=filter_function
        )

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
