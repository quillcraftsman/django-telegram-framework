from telegram_framework import actions
from telegram_framework.messages import Message


def send_hello_message(bot, message):
    hello_message = Message('hello', sender=bot)
    return actions.send_message(message.chat, hello_message)
