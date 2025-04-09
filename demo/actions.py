from pathlib import Path
from django.template.loader import render_to_string
from django.conf import settings
from telegram_framework import actions
from telegram_framework import messages, media
from .models import create_info_text


def send_bot_info(bot, message):
    text = create_info_text(message.text)
    info_message = messages.create_message(
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
    response_message = messages.create_message(
        response_text, sender=bot, format_type='HTML'
    )
    return actions.send_message(message.chat, response_message)


def load_picture_example(bot, message):
    file_path = Path(settings.BASE_DIR) / 'static' / 'logo_1280_640.png'
    caption = messages.create_message('<b>DTF</b> LOGO', bot, format_type='HTML')
    image = media.create_image(bot, file_path, caption)
    return actions.send_image(message.chat, image)
