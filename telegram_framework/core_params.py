import functools
from typing import Callable
from django.urls.resolvers import RoutePattern
from telegram_framework.messages import Call, Message


def match_function(pattern, message_data: str):
    route_pattern = RoutePattern(pattern)
    return route_pattern.match(message_data)


def prepare_handler(handler_function: Callable, match_function_: Callable):

    @functools.wraps(handler_function)
    def inner(bot, message, *args, **kwargs):
        _, _, params = '', (), {}
        _, _, params = match_function_(message)
        kwargs = kwargs | params
        return handler_function(bot, message, *args, **kwargs)

    return inner


def get_call_match_function(pattern):

    def inner(call: Call):
        message_data = call.data
        return match_function(pattern, message_data)

    return inner


def get_command_match_function(pattern):

    def inner(message: Message):
        message_data = message.text
        return match_function(pattern, message_data)

    return inner
