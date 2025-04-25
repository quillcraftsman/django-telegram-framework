from pathlib import Path
from django.template.loader import render_to_string
from django.conf import settings
from telegram_framework import actions, messages, use, keyboards
from demo.models import Faq


def send_bot_info(bot, message):
    text = render_to_string('demo/bot/start.html')
    info_message = messages.create_message(
        text, sender=bot, format_type='HTML'
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


# START list_action_example
list_action_example = use.list_action(
    Faq,
    template_name='demo/bot/list.html',
)
# END list_action_example


# START template_action_example
template_action_example = use.template_action(
    'demo/bot/reply.html',
    context={
        'this': 'Это',
        'message': 'сообщение',
        'make': 'было создано по шаблону'
    }
)
# END template_action_example


# START message_with_inline_keyboard_example
def message_with_inline_keyboard_example(bot, message):
    keyboard = keyboards.inline.Keyboard(
        buttons=[
            keyboards.inline.Button('Нажми меня', 'put_on_me'),
        ]
    )
    message_with_text = messages.create_message('Пример сообщения с кнопкой', sender=bot)
    message_with_keyboard = messages.add_keyboard(message_with_text, keyboard)
    return actions.send_message(message.chat, message_with_keyboard)


def put_button_handler(bot, message):
    reply_message = messages.create_message(
        text='Вы нажали кнопку, а я обработал нажатие',
        sender=bot,
    )
    return actions.send_message(message.chat, reply_message)
# END message_with_inline_keyboard_example
