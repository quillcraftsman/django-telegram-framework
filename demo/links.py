from telegram_framework import links
from . import actions


bot_links = [
    links.on_command(actions.send_bot_info, 'start'),
    links.on_command(actions.send_bot_info, 'help'),
    links.on_message(actions.echo_answer),
]
