from pathlib import Path
from django.template.loader import render_to_string
from django.conf import settings
from telegram_framework import actions, messages, use, keyboards, bots
from telegram_framework.keyboards import layouts
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


# START list_action_example
list_action_example = use.list_action(
    Faq,
    template_name='demo/bot/list.html',
)
# END list_action_example


# START list_action_pagination_example
list_action_pagination_example = use.list_action(
    Faq,
    template_name='demo/bot/list.html',
    pagination=use.list.Pagination(1, call_data_pattern='list_action_pagination {page}')
)
# END list_action_pagination_example


# START detail_action_example
detail_action_example = use.detail_action(
    Faq,
    'demo/bot/detail.html',
)
# END detail_action_example


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


# START message_with_reply_keyboard_example
def message_with_reply_keyboard_example(bot, message):
    keyboard = keyboards.reply.Keyboard(
        name = 'Пример клавиатуры',
        buttons=[
            keyboards.reply.Button('Нажми меня 🔍'),
        ]
    )
    message_with_text = messages.create_message('Пример сообщения с клавиатурой', sender=bot)
    message_with_keyboard = messages.add_keyboard(message_with_text, keyboard)
    return actions.send_message(message.chat, message_with_keyboard)


def put_keyboard_handler(bot, message):
    reply_message = messages.create_message(
        text='Вы нажали на клавиатуру, а я обработал нажатие и убрал клавиатуру',
        sender=bot,
    )
    reply_message = messages.add_keyboard(reply_message, keyboards.reply.EmptyKeyboard())
    return actions.send_message(message.chat, reply_message)
# END message_with_reply_keyboard_example


# START complex_message_example
def complex_message_example(bot, message):
    first_message = messages.create_message(
        text='Первая часть сообщения',
        sender=bot,
    )
    keyboard = keyboards.reply.Keyboard(
        name='Пример клавиатуры',
        buttons=[
            keyboards.reply.Button('Нажми меня 🔍'),
        ]
    )
    first_message = messages.add_keyboard(first_message, keyboard)
    chat = actions.send_message(message.chat, first_message)

    file_path = Path(settings.BASE_DIR) / 'static' / 'logo_1280_640.png'
    caption = messages.create_message(
        'Пример <b>комплексного</b> сообщения',
        bot,
        format_type='HTML'
    )
    image = messages.create_image(bot, file_path, caption)

    keyboard = keyboards.inline.Keyboard(
        buttons=[
            keyboards.inline.Button('Нажми меня', 'put_on_me'),
        ]
    )
    image = messages.add_keyboard(image, keyboard)
    return actions.send_image(chat, image)
# END complex_message_example


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


# START sequence_example
def start_sequence_example(bot, message):
    keyboard = keyboards.force.Keyboard()
    message_with_text = messages.create_message('Как бы вас звали на букву "Л"?:', sender=bot)
    message_with_keyboard = messages.add_keyboard(message_with_text, keyboard)
    chat = actions.send_message(message.chat, message_with_keyboard)
    chat = bots.register_next_step_handler(bot, chat, sequence_first_name_example)
    return chat


def sequence_first_name_example(bot, message):
    first_name = message.text
    if first_name.startswith('Л'):
        keyboard = keyboards.force.Keyboard()
        message_with_text = messages.create_message('Какой бы была ваша фамилия на букву "Л"?:', sender=bot)
        message_with_keyboard = messages.add_keyboard(message_with_text, keyboard)
        chat = actions.send_message(message.chat, message_with_keyboard)
        chat = bots.register_next_step_handler(bot, chat, sequence_last_name_example)
        return chat

    keyboard = keyboards.force.Keyboard()
    message_with_text = messages.create_message(
        'Неверно введено имя, пожалуйста введите снова:',
        sender=bot
    )
    message_with_keyboard = messages.add_keyboard(message_with_text, keyboard)
    chat = actions.send_message(message.chat, message_with_keyboard)
    chat = bots.register_next_step_handler(bot, chat, sequence_first_name_example)
    return chat


def sequence_last_name_example(bot, message):
    last_name = message.text
    if last_name.startswith('Л'):
        # Event sourcing
        for old_message in reversed(message.chat.messages[:-1]):
            if old_message.text.startswith('Л'):
                break
        first_name = old_message
        result_text = f'Привет, {first_name} {last_name}'
        message_with_text = messages.create_message(result_text, sender=bot)
        chat = actions.send_message(message.chat, message_with_text)
        return chat

    keyboard = keyboards.force.Keyboard()
    message_with_text = messages.create_message(
        'Неверно введена фамилия, пожалуйста введите снова:',
        sender=bot
    )
    message_with_keyboard = messages.add_keyboard(message_with_text, keyboard)
    chat = actions.send_message(message.chat, message_with_keyboard)
    chat = bots.register_next_step_handler(bot, chat, sequence_last_name_example)
    return chat
# END param_call_buttons_example
