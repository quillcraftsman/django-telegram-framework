from telegram_framework import actions
from telegram_framework.messages import Message, create_reply


def send_bot_info(bot, message):
    text = (f'Привет. Я Demo Telegram Bot. '
            f'Я создан на основе Django Telegram Framework. '
            f'Я могу познакомить'
             f'тебя с основными функциями библиотеки. '
            f'Например сейчас ты отправил команду {message.text} и видишь'
             f'это сообщение')
    info_message = Message(
        text, sender=bot
    )
    return actions.send_message(message.chat, info_message)


def echo_answer(bot, message):
    text = f'На любое неизвестное сообщение я умею присылать его в ответ: {message.text}'
    echo_reply = create_reply(message, text, bot)
    return actions.send_reply(echo_reply)
