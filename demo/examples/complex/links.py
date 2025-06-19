from telegram_framework import links
from . import examples


bot_links = [
    links.on_command(
        examples.complex_message_example,
        'complex_message',
        'Пример всех функций в одном месте'
    ),
]
