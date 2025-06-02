import functools
from django.urls.resolvers import RoutePattern


def prepare_handler(handler_function, pattern):

    @functools.wraps(handler_function)
    def inner(bot, message, *args, **kwargs):
        _, _, params = '', (), {}
        match_function = get_match_function(pattern)
        _, _, params = match_function(message)
        kwargs = kwargs | params
        return handler_function(bot, message, *args, **kwargs)

    return inner


def _match_function(message, pattern):
    route_pattern = RoutePattern(f'/{pattern}')
    return route_pattern.match(message.text)


def _filter_function(message, pattern):
    match_result = _match_function(message, pattern)
    if match_result is None:
        return False
    text, _, _ = match_result
    if text != '':
        return False
    return True


def get_filter_function(pattern):

    def inner(message):
        return _filter_function(message, pattern)

    return inner


def get_match_function(pattern):

    def inner(message):
        return _match_function(message, pattern)

    return inner
