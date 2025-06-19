from telegram_framework import links
from . import examples


bot_links = [
    links.on_command(
        examples.start_sequence_example,
        'sequence_example',
        'Последовательность ввода данных',
        # next_steps=[actions.sequence_last_name_example]
    ),
]
