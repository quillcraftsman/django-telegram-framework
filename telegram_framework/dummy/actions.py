from telegram_framework.chat import add_message, Chat
from telegram_framework.messages import Message, Reply


def send_reply(reply: Reply):
    return add_message(reply.message.chat, reply)


def send_message(chat: Chat, message: Message):
    chat = add_message(chat, message)
    return chat
    # last_message = get_last_message(chat)
    # for bot in chat.bots:
    #     if last_message:
    #         if last_message.sender != bot:
    #             chat = handle_message(bot, last_message
