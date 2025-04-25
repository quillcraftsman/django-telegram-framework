from telegram_framework import bots, messages, actions
from .description import get_description


def _base_commands(bot, message, str_format='{name} - {description}'):
    commands_list = bots.get_commands_list(bot)
    if not commands_list:
        message_text = '-'
    else:
        commands_str_list = []
        for name, handler in commands_list:
            command_str = str_format.format(name=name, description=get_description(handler))
            commands_str_list.append(command_str)
        message_text = '\n'.join(commands_str_list)
    command_message = messages.create_message(
        message_text,
        sender=bot,
    )
    return actions.send_message(message.chat, command_message)


def bot_father_commands(bot, message):
    return _base_commands(bot, message, '{name} - {description}')


def user_commands(bot, message):
    return _base_commands(bot, message, '/{name} - {description}')
