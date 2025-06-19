from telegram_framework import links
from . import examples


bot_links = [
    links.on_command(
        examples.message_with_inline_keyboard_example,
        'message_with_inline_keyboard', 'Сообщение с кнопкой'
    ),
    links.on_command(
        examples.message_with_reply_keyboard_example,
        'message_with_reply_keyboard',
        'Сообщение с клавиатурой',
    ),
    links.on_text(
        examples.put_keyboard_handler,
        'Нажми меня 🔍'
    ),
    links.on_call(
        examples.put_button_handler, 'put_on_me'
    ),
]
