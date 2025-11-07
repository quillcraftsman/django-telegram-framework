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

# Дублируется в Telebot, зависит от message надо перенести в core пакет
def _get_parse_mode(message):
    parse_mode = message.format_type if message.format_type != 'text' else None
    return parse_mode

def send_message(chat: chats.Chat, message: messages.Message):
    parse_mode = _get_parse_mode(message)
    return _send_message(chat, message, parse_mode)
