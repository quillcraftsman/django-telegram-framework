from django.template.loader import render_to_string
from telegram_framework import actions
from telegram_framework import messages
from .models import create_info_text


def send_bot_info(bot, message):
    text = create_info_text(message.text)
    info_message = messages.Message(
        text, sender=bot
    )
    return actions.send_message(message.chat, info_message)


def echo_answer(bot, message):
    text = f'На любое неизвестное сообщение я умею присылать его в ответ: {message.text}'
    echo_reply = messages.create_reply(message, text, bot)
    return actions.send_reply(echo_reply)


def render_template_example(bot, message):
    reply_template = 'demo/bot/reply.html'
    context = {
        'this': 'Это',
        'message': 'сообщение',
        'make': 'было создано по шаблону'
    }
    response_text = render_to_string(reply_template, context)
    response_message = messages.Message(
        response_text, sender=bot
    )
    return actions.send_html_message(message.chat, response_message)
