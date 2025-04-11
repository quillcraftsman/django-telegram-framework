from pathlib import Path
from django.template.loader import render_to_string
from django.conf import settings
from telegram_framework import actions
from telegram_framework import messages


def send_bot_info(bot, message):
    text = render_to_string('demo/bot/start.html')
    info_message = messages.create_message(
        text, sender=bot, format_type='HTML'
    )
    return actions.send_message(message.chat, info_message)


def commands_info(bot, message):

    commands = {
        '/help': 'Информация обо мне',
        '/commands': 'Список примеров (что можно сделать с помощью DTF)',
        '/text_message': 'Отправка текстового сообщения',
        '/html_message': 'Отправка html сообщения',
        '/render_template': 'Форматирование по шаблону',
        '/send_picture': 'Отправка картинки',
        '/send_picture_with_caption': 'Отправка картинки с заголовком',
        '/send_picture_with_html_caption': 'Отправка картинки с HTML заголовком',
        'любое сообщение': 'Ответ на это сообщение',
    }
    text = render_to_string('demo/bot/commands.html', {'commands': commands})
    commands_message = messages.create_message(
        text, sender=bot, format_type='HTML'
    )
    return actions.send_message(message.chat, commands_message)


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
    context = {
        'this': 'Это',
        'message': 'сообщение',
        'make': 'было создано по шаблону'
    }
    response_message = messages.create_template_message(
        sender=bot,
        template='demo/bot/reply.html',
        context=context,
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
