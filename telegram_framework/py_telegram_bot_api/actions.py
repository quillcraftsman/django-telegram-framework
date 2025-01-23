from telegram_framework.chat import add_message, Chat
from telegram_framework.messages import Message, Reply


def send_reply(reply: Reply):
    message = reply.message
    text = reply.text
    chat = message.chat
    bot = reply.sender
    bot.reply_to(message, text)
    chat = Chat(id=chat.id)
    return add_message(chat, reply)


def send_message(chat: Chat, message: Message):
    bot = message.sender
    text = message.text
    bot.send_message(
        chat.id,
        text,
    )
    chat = Chat(id=chat.id)
    return add_message(chat, message)
