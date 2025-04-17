from telegram_framework import bots, messages, actions
from .description import get_description


def get_commands(bot, message):
    commands_list = bots.get_commands_list(bot)
    if not commands_list:
        message_text = '-'
    else:
        commands_str_list = []
        for name, handler in commands_list:
            command_str = f'{name} - {get_description(handler)}'
            commands_str_list.append(command_str)
        message_text = '\n'.join(commands_str_list)
    command_message = messages.create_message(
        message_text,
        sender=bot,
    )
    return actions.send_message(message.chat, command_message)
