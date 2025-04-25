import functools


def prepare_handler(handler_function, bot):

    @functools.wraps(handler_function)
    def inner(*args, **kwargs):
        return handler_function(bot, *args, **kwargs)

    return inner


def prepare_call_handler(handler_function, bot):

    @functools.wraps(handler_function)
    def inner(call):
        message = call.message
        return handler_function(bot, message)

    return inner
