from telegram_framework import links
from . import actions

bot_links = [
    links.on_command(actions.bot_father_commands, 'bot_father_commands'),
    links.on_command(actions.user_commands, 'commands'),
]
