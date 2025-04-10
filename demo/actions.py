from pathlib import Path
from django.template.loader import render_to_string
from django.conf import settings
from telegram_framework import actions
from telegram_framework import messages
from .models import create_info_text


def send_bot_info(bot, message):
    text = create_info_text(message.text)
    info_message = messages.create_message(
        text, sender=bot
    )
    return actions.send_message(message.chat, info_message)


# START send_text_message_example
def send_text_message_example(bot, message):
    text = 'Пример отправки обычного текстового сообщения'
    text_message = messages.create_message(
        text=text,
        sender=bot,
    )
    return actions.send_message(message.chat, text_message)
# END send_text_message_example


# START send_html_message_example
def send_html_message_example(bot, message):
    text = '<b>Пример</b> <i>отправки</i> <s>текстового</s> HTML сообщения'
    text_message = messages.create_message(
        text=text,
        sender=bot,
        format_type='HTML',
    )
    return actions.send_message(message.chat, text_message)
# END send_html_message_example


# START render_template_example
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
# END render_template_example


# START echo_answer_example
def echo_answer_example(bot, message):
    text = f'На любое неизвестное сообщение я умею присылать его в ответ: {message.text}'
    echo_reply = messages.create_reply(message, text, bot)
    return actions.send_reply(echo_reply)
# END echo_answer_example


# START send_picture_example
def send_picture_example(bot, message):
    file_path = Path(settings.BASE_DIR) / 'static' / 'logo_1280_640.png'
    image = messages.create_image(bot, file_path)
    return actions.send_image(message.chat, image)
# END send_picture_example


# START send_picture_with_caption_example
def send_picture_with_caption_example(bot, message):
    file_path = Path(settings.BASE_DIR) / 'static' / 'logo_1280_640.png'
    caption = messages.create_message('Это логотипы DTF', bot)
    image = messages.create_image(bot, file_path, caption)
    return actions.send_image(message.chat, image)
# END send_picture_with_caption_example


# START send_picture_with_html_caption_example
def send_picture_with_html_caption_example(bot, message):
    file_path = Path(settings.BASE_DIR) / 'static' / 'logo_1280_640.png'
    caption = messages.create_message(
        'Это логотипы <b>DTF</b>',
        bot,
        format_type='HTML'
    )
    image = messages.create_image(bot, file_path, caption)
    return actions.send_image(message.chat, image)
# END send_picture_with_html_caption_example
