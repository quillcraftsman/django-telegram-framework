from telegram_framework import chats, messages, media


def send_reply(reply: messages.Reply):
    return chats.add_message(reply.chat, reply)


def send_message(chat: chats.Chat, message: messages.Message):
    chat = chats.add_message(chat, message)
    return chat


def send_image(chat: chats.Chat, image: media.Image):
    chat = chats.add_message(chat, image.caption)
    return chat
