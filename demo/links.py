from telegram_framework import links
from . import actions

bot_links = links.include([], 'telegram_framework.commands.links')

bot_links += [
    links.on_command(actions.send_bot_info, 'start', 'Начать общение с ботом'),
    links.on_command(actions.send_bot_info, 'help', 'Получить информацию о боте'),
]

bot_links = links.include_all(
    bot_links,
    [
        'demo.examples.keyboard.links',
        'demo.examples.fba.links',
        'demo.examples.complex.links',
        'demo.examples.sequence.links',
        'demo.examples.base.links',
    ]
)
