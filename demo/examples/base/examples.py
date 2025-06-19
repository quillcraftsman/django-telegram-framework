from pathlib import Path
from django.conf import settings
from telegram_framework import  messages, actions, keyboards
from telegram_framework.keyboards import layouts


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


# START fixed_text_answer_example
def fixed_text_answer_example(bot, message):
    text = f'На сообщение {message.text}, я даю фиксированный ответ: Пожалуйста'
    reply = messages.create_reply(message, text, bot)
    return actions.send_reply(reply)
# END fixed_text_answer_example


# START contains_text_answer_example
def contains_text_answer_example(bot, message):
    text = 'На сообщение содержащее "Привет", я говорю "И тебе привет"'
    reply = messages.create_reply(message, text, bot)
    return actions.send_reply(reply)
# END contains_text_answer_example


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


# START send_param_text_message_example
def send_param_text_message_example(bot, message, param):
    text = f'Пример отправки обычного текстового сообщения с параметром "{param}"'
    text_message = messages.create_message(
        text=text,
        sender=bot,
    )
    return actions.send_message(message.chat, text_message)
# END send_param_text_message_example


# START param_call_buttons_example
def param_call_buttons_example(bot, message):
    keyboard = keyboards.inline.Keyboard(
        buttons=[
            keyboards.inline.Button('Параметр ONE', 'put_on_me_params ONE'),
            keyboards.inline.Button('Параметр TWO', 'put_on_me_params TWO'),
        ],
        layout=layouts.Layout(columns_count=2)
    )
    message_with_text = messages.create_message('Кнопки для обработчика с параметром', sender=bot)
    message_with_keyboard = messages.add_keyboard(message_with_text, keyboard)
    return actions.send_message(message.chat, message_with_keyboard)


def put_button_param_handler(bot, message, param):
    reply_message = messages.create_message(
        text=f'Реакция на параметр {param}',
        sender=bot,
    )
    return actions.send_message(message.chat, reply_message)
# END param_call_buttons_example


# START get_user_id_example
def get_user_id_example(bot, message):
    user = message.sender
    user_id = user.id
    response_message = messages.create_message(
        text=f'Ваш telegram id: {user_id}',
        sender=bot,
    )
    return actions.send_message(message.chat, response_message)
# END get_user_id_example
