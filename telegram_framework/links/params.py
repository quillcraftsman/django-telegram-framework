import functools
from . import call_params, command_params


def prepare_handler(handler_function, pattern, function_type):

    @functools.wraps(handler_function)
    def inner(bot, message, *args, **kwargs):
        _, _, params = '', (), {}
        match_function = get_match_function(pattern, function_type)
        _, _, params = match_function(message)
        kwargs = kwargs | params
        return handler_function(bot, message, *args, **kwargs)

    return inner


def _filter_function(message, pattern, function_type):
    match_function = get_match_function(pattern, function_type)
    match_result = match_function(message)
    if match_result is None:
        return False
    text, _, _ = match_result
    if text != '':
        return False
    return True


def get_filter_function(pattern, function_type):

    def inner(message):
        return _filter_function(message, pattern, function_type)

    return inner


def get_match_function(pattern, function_type):

    def inner(message):
        mapper = {
            'command': command_params.get_match_function,
            'call': call_params.get_match_function,
        }
        match_function = mapper[function_type](pattern)
        return match_function(message)

    return inner
