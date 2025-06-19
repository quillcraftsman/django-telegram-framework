from telegram_framework import links
from . import examples


bot_links = [
    links.on_command(
        examples.start_sequence_example,
        'sequence_example',
        'Последовательность ввода данных',
    ),
    links.on_command(
        examples.start_sequence_form_example,
        'sequence_form_example',
        'Последовательность ввода данных (Django Формы)',
    ),
]
