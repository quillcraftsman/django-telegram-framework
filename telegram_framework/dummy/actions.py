from telegram_framework.chat import add_message, Chat
from telegram_framework.messages import Message, Reply


def send_reply(reply: Reply):
    return add_message(reply.message.chat, reply)


def send_message(chat: Chat, message: Message):
    return add_message(chat, message)
