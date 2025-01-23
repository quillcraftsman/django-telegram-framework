from telegram_framework import links
from . import actions


bot_links = [
    links.on_command(actions.send_hello_message, 'hello'),
    links.on_command(actions.send_hello_as_reply, 'reply_me'),
]
