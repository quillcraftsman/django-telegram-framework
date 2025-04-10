from telegram_framework import chats, messages


def send_reply(reply: messages.Reply):
    return chats.add_message(reply.chat, reply)


def send_message(chat: chats.Chat, message: messages.Message):
    chat = chats.add_message(chat, message)
    return chat


def send_image(chat: chats.Chat, image: messages.Image):
    chat = chats.add_message(chat, image)
    return chat
