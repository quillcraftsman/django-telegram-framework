from typing import Callable
from telegram_framework import core_params



def _get_filter_function(pattern):

    def inner(message: str):
        match_result = core_params.match_function(pattern, message)
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
    filter_function = _get_filter_function(params_pattern)
    return handler, filter_function


def get_param_command_handler(params_pattern, handler: Callable):
    match_function = core_params.get_command_match_function(params_pattern)
    handler = core_params.prepare_handler(handler, match_function)
    filter_function = _get_filter_function(params_pattern)
    return handler, filter_function
