from telegram_framework.messages.text_message import Message


def create_chat_message(message: Message, chat):
    return Message(
        text=message.text,
        sender=message.sender,
        chat=chat,
    )


def is_chat_message(message):
    return hasattr(message, 'chat') and message.chat is not None
