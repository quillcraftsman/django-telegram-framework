from telegram_framework import chats, messages, bots


def send_reply(reply: messages.Reply):
    return chats.add_message(reply.chat, reply)


def send_message(chat: chats.Chat, message: messages.Message):
    chat = chats.add_message(chat, message)
    return chat


def send_image(chat: chats.Chat, image: messages.Image):
    chat = chats.add_message(chat, image)
    return chat


def wait_response(bot, chat, handler):
    chat = bots.register_next_step_handler(bot, chat, handler)
    return chat
