from dataclasses import replace


def create_chat_message(message, chat):
    return replace(message, chat=chat)


def is_chat_message(message):
    return hasattr(message, 'chat') and message.chat is not None
