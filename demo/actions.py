from telegram_framework import actions
from telegram_framework.messages import Message, Reply


def send_hello_message(bot, message):
    hello_message = Message('hello', sender=bot)
    return actions.send_message(message.chat, hello_message)


def send_hello_as_reply(bot, message):
    hello_reply = Reply('hello', sender=bot, message=message)
    return actions.send_reply(hello_reply)
