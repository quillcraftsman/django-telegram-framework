from telegram_framework import chats
from telegram_framework.messages import Message, Reply


def send_reply(reply: Reply):
    return chats.add_message(reply.message.chat, reply)


def send_message(chat: chats.Chat, message: Message):
    chat = chats.add_message(chat, message)
    return chat
