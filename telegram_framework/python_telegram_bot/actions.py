from telegram.ext.updater import Updater
from telegram_framework import chats, messages


def _send_message(chat: chats.Chat, message: messages.Message, parse_mode=None):
    bot: Updater = message.sender
    text = message.text
    bot.bot.send_message(
        chat.id,
        text,
        parse_mode=parse_mode,
    )
    return chats.add_message(chat, message)


def send_message(chat: chats.Chat, message: messages.Message):
    return _send_message(chat, message, None)
