import functools
from telebot import types
from telegram_framework import messages, chats


def to_call(callback_query: types.CallbackQuery):
    pure_message = messages.create_call(
        callback_query.from_user,
        data=callback_query.data
    )
    # Тут похоже нужно еще как то восстановить чат
    chat = to_chat(callback_query.message.chat)
    chat = chats.save_message(chat, pure_message)
    # chat_message = messages.create_chat_message(pure_message, chat)
    chat_message = chats.get_last_message(chat)
    # chat_message = messages.create_chat_message(pure_message, callback_query.message.chat)
    return chat_message


CHAT_STORE = {}


def to_chat(telebot_chat: types.Chat):
    chat_id = telebot_chat.id
    chat = CHAT_STORE.get(
        chat_id,
        chats.Chat(
            id=telebot_chat.id,
        )
    )
    return chat


def to_message(telebot_message: types.Message):
    pure_message = messages.create_message(
        telebot_message.text,
        sender=telebot_message.from_user,
        format_type=telebot_message.reply_markup,
        message_id=telebot_message.message_id,
    )
    # Тут похоже нужно еще как то восстановить чат
    chat = to_chat(telebot_message.chat)
    chat = chats.save_message(chat, pure_message)
    # chat_message = messages.create_chat_message(pure_message, chat)
    chat_message = chats.get_last_message(chat)
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


def adapt_data(message, handler_function, bot, *args, **kwargs):
    message = prepare_message(message)
    result_chat = handler_function(bot, message, *args, **kwargs)
    CHAT_STORE[result_chat.id] = result_chat
    return result_chat


def prepare_handler(handler_function, bot):

    @functools.wraps(handler_function)
    def inner(message, *args, **kwargs):
        # message = prepare_message(message)
        # result_chat = handler_function(bot, message, *args, **kwargs)
        # CHAT_STORE[result_chat.id] = result_chat
        # return result_chat
        return adapt_data(message, handler_function, bot, *args, **kwargs)

    return inner


def prepare_call_handler(handler_function, bot):

    @functools.wraps(handler_function)
    def inner(call):
        # message = prepare_message(call)
        # result_chat = handler_function(bot, message)
        # CHAT_STORE[result_chat.id] = result_chat
        # return result_chat
        return adapt_data(call, handler_function, bot)

    return inner
