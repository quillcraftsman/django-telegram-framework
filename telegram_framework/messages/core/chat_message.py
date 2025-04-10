from telegram_framework.functions import update


def create_chat_message(message, chat):
    return update(message, chat=chat)


def is_chat_message(message):
    return hasattr(message, 'chat') and message.chat is not None
