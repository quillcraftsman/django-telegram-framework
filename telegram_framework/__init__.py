# pylint: disable=wrong-import-position
from django.conf import settings

bot_type = settings.TELEGRAM_BOT_TYPE

if bot_type == 'Dummy':
    from .dummy.bot import (
        get_bot, find_handler,
        handle_message,
        start,
        register_command_handler,
        register_message_handler
    )
    from .dummy import actions
elif bot_type == 'pyTelegramBotAPI':  # pragma: no cover
    from .py_telegram_bot_api.bot import (
        get_bot, find_handler,
        handle_message,
        start,
        register_command_handler,
        register_message_handler
    )
    from .py_telegram_bot_api import actions

from . import links
