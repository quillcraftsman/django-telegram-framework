from telegram_framework import links
from .actions import send_hello_message


bot_links = [
    links.on_command(send_hello_message, 'hello'),
]