import functools
from telebot import types
from telegram_framework import messages


def prepare_message(telebot_message: types.Message) -> messages.Message:
    if not isinstance(telebot_message, types.Message):
        return telebot_message
    pure_message = messages.create_message(
        telebot_message.text,
        sender=telebot_message.from_user,
        format_type=telebot_message.reply_markup,
    )
    chat_message = messages.create_chat_message(pure_message, telebot_message.chat)
    return chat_message


def prepare_handler(handler_function, bot):

    # @functools.wraps(handler_function)
    # def inner(*args, **kwargs):
    #     return handler_function(bot, *args, **kwargs)
    @functools.wraps(handler_function)
    def inner(message, *args, **kwargs):
        message = prepare_message(message)
        return handler_function(bot, message, *args, **kwargs)

    return inner


def prepare_call_handler(handler_function, bot):

    @functools.wraps(handler_function)
    def inner(call):
        message = call.message
        message = prepare_message(message)
        return handler_function(bot, message)

    return inner
