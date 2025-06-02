import functools
from telebot import types
from telegram_framework import messages


def to_call(callback_query: types.CallbackQuery):
    pure_message = messages.create_call(
        callback_query.from_user,
        data=callback_query.data
    )
    chat_message = messages.create_chat_message(pure_message, callback_query.message.chat)
    return chat_message


def to_message(telebot_message: types.Message):
    pure_message = messages.create_message(
        telebot_message.text,
        sender=telebot_message.from_user,
        format_type=telebot_message.reply_markup,
        message_id=telebot_message.message_id,
    )
    chat_message = messages.create_chat_message(pure_message, telebot_message.chat)
    return chat_message


def prepare_message(telebot_message):

    instance_mapper = {
        types.CallbackQuery: to_call,
        types.Message: to_message,
    }

    current_type_function = instance_mapper.get(type(telebot_message))
    if current_type_function:
        return current_type_function(telebot_message)

    return telebot_message


def prepare_handler(handler_function, bot):

    @functools.wraps(handler_function)
    def inner(message, *args, **kwargs):
        message = prepare_message(message)
        return handler_function(bot, message, *args, **kwargs)

    return inner


def prepare_call_handler(handler_function, bot):

    @functools.wraps(handler_function)
    def inner(call):
        message = prepare_message(call)
        return handler_function(bot, message)

    return inner
