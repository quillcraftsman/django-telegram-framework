from telegram_framework import chats, messages


def send_reply(reply: messages.Reply):
    message = reply.message
    text = reply.text
    chat = message.chat
    bot = reply.sender
    bot.reply_to(message, text)
    chat = chats.Chat(id=chat.id)
    return chats.add_message(chat, reply)


def _send_message(chat: chats.Chat, message: messages.Message, parse_mode=None):
    bot = message.sender
    text = message.text
    bot.send_message(
        chat.id,
        text,
        parse_mode=parse_mode,
    )
    chat = chats.Chat(id=chat.id)
    return chats.add_message(chat, message)


def send_message(chat: chats.Chat, message: messages.Message):
    return _send_message(chat, message)


def send_html_message(chat: chats.Chat, message: messages.Message):
    return _send_message(chat, message, parse_mode='HTML')
