import functools
from typing import Callable
from django.urls.resolvers import RoutePattern
from telegram_framework.messages import Call, Message


def _match_function(pattern, message_data: str):
    route_pattern = RoutePattern(pattern)
    return route_pattern.match(message_data)


def _prepare_command_handler(handler_function: Callable, match_function: Callable):

    @functools.wraps(handler_function)
    def inner(bot, message: Message, *args, **kwargs):
        _, _, params = '', (), {}
        _, _, params = match_function(message)
        kwargs = kwargs | params
        return handler_function(bot, message, *args, **kwargs)

    return inner


def _prepare_call_handler(handler_function: Callable, match_function: Callable):
    # Для Dummy call и command одинаковые
    return _prepare_command_handler(handler_function, match_function)


def _get_filter_function(pattern):

    def inner(message: str):
        match_result = _match_function(pattern, message)
        if match_result is None:
            return False
        text, _, _ = match_result
        if text != '':
            return False
        return True

    return inner


def _get_call_match_function(pattern):

    def inner(call: Call):
        message_data = call.data
        return _match_function(pattern, message_data)

    return inner


def _get_command_match_function(pattern):

    def inner(message: Message):
        message_data = message.text
        return _match_function(pattern, message_data)

    return inner


def get_param_call_handler(params_pattern, handler: Callable):
    match_function = _get_call_match_function(params_pattern)
    handler = _prepare_call_handler(handler, match_function)
    filter_function = _get_filter_function(params_pattern)
    return handler, filter_function


def get_param_command_handler(params_pattern, handler: Callable):
    match_function = _get_command_match_function(params_pattern)
    handler = _prepare_command_handler(handler, match_function)
    filter_function = _get_filter_function(params_pattern)
    return handler, filter_function
