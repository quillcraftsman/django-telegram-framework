from typing import Callable
from telegram_framework import core_params


def _get_filter_function(match_function: Callable):

    def inner(message):
        match_result = match_function(message)
        if match_result is None:
            return False
        text, _, _ = match_result
        if text != '':
            return False
        return True

    return inner


def get_param_call_handler(params_pattern, handler: Callable):
    match_function = core_params.get_call_match_function(params_pattern)
    handler = core_params.prepare_handler(handler, match_function)
    filter_function = _get_filter_function(match_function)
    return handler, filter_function


def get_param_command_handler(params_pattern, handler: Callable):
    match_function = core_params.get_command_match_function(params_pattern)
    handler = core_params.prepare_handler(handler, match_function)
    filter_function = _get_filter_function(match_function)
    return handler, filter_function
