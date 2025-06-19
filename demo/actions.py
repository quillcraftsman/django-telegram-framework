from django.template.loader import render_to_string
from telegram_framework import actions, messages


def send_bot_info(bot, message):
    text = render_to_string('demo/bot/start.html')
    info_message = messages.create_message(
        text, sender=bot, format_type='HTML'
    )
    return actions.send_message(message.chat, info_message)
