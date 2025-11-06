import functools
from telegram.update import Update
from telegram.user import User
from telegram.chat import Chat
from telegram_framework import user, messages, chats

CHAT_STORE = {}

def to_user_data(from_user: User)->user.UserData:
    user_data = user.UserData(
        id = from_user.id,
        first_name=from_user.first_name,
        last_name=from_user.last_name,
        username=from_user.username,
    )
    return user_data


# Это по идее должен быть интерфейс DummyBot
class Sender:
    def __init__(self, user_data):
        self.user_data = user_data


def to_chat(ptb_chat: Chat):
    chat_id = ptb_chat.id
    chat = CHAT_STORE.get(
        chat_id,
        chats.Chat(
            id=ptb_chat.id,
        )
    )
    return chat


def to_message(update: Update):
    user_data = to_user_data(update.message.from_user)
    sender = Sender(user_data)
    pure_message = messages.create_message(
        update.message.text,
        sender=sender,
        format_type=update.message.reply_markup,
        message_id=update.message.message_id,
    )
    # Тут похоже нужно еще как то восстановить чат
    chat = to_chat(update.message.chat)
    chat = chats.save_message(chat, pure_message)
    # chat_message = messages.create_chat_message(pure_message, chat)
    chat_message = chats.get_last_message(chat)
    return chat_message


def prepare_message(update):
    return to_message(update)


def adapt_data(update, handler_function, bot, *args, **kwargs):
    message = prepare_message(update)
    result_chat = handler_function(bot, message, *args, **kwargs)
    CHAT_STORE[result_chat.id] = result_chat
    return result_chat


def prepare_handler(handler_function, bot):

    @functools.wraps(handler_function)
    def inner(update, context, *args, **kwargs):  # pylint:disable=(unused-argument)
        return adapt_data(update, handler_function, bot, *args, **kwargs)

    return inner
