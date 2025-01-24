from telegram_framework import chats
from telegram_framework.messages import Message, Reply


def send_reply(reply: Reply):
    message = reply.message
    text = reply.text
    chat = message.chat
    bot = reply.sender
    bot.reply_to(message, text)
    chat = chats.Chat(id=chat.id)
    return chats.add_message(chat, reply)


def send_message(chat: chats.Chat, message: Message):
    bot = message.sender
    text = message.text
    bot.send_message(
        chat.id,
        text,
    )
    chat = chats.Chat(id=chat.id)
    return chats.add_message(chat, message)
