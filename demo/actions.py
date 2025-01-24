from telegram_framework import actions
from telegram_framework.messages import Message, create_reply
from .models import create_info_text

def send_bot_info(bot, message):
    text = create_info_text(message.text)
    info_message = Message(
        text, sender=bot
    )
    return actions.send_message(message.chat, info_message)


def echo_answer(bot, message):
    text = f'На любое неизвестное сообщение я умею присылать его в ответ: {message.text}'
    echo_reply = create_reply(message, text, bot)
    return actions.send_reply(echo_reply)
