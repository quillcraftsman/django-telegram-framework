import functools
from django.urls.resolvers import RoutePattern


def _match_function(pattern, message_data):
    route_pattern = RoutePattern(pattern)
    return route_pattern.match(message_data)


def prepare_command_handler(handler_function, match_function):

    @functools.wraps(handler_function)
    def inner(bot, message, *args, **kwargs):
        _, _, params = '', (), {}
        _, _, params = match_function(message)
        kwargs = kwargs | params
        return handler_function(bot, message, *args, **kwargs)

    return inner


def prepare_call_handler(handler_function, match_function):
    # Для Telebot call и command одинаковые
    return prepare_command_handler(handler_function, match_function)


def get_filter_function(match_function):

    def inner(message):
        match_result = match_function(message)
        if match_result is None:
            return False
        text, _, _ = match_result
        if text != '':
            return False
        return True

    return inner


def get_call_match_function(pattern):

    def inner(message):
        message_data = message.data
        return _match_function(pattern, message_data)

    return inner


def get_command_match_function(pattern):

    def inner(message):
        message_data = message.text
        return _match_function(pattern, message_data)

    return inner
