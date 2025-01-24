# pylint: disable=wrong-import-position
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

try:
    BOT_TYPE = settings.TELEGRAM_BOT_TYPE
except ImproperlyConfigured:  # pragma: no cover
    BOT_TYPE = 'Dummy'

if BOT_TYPE == 'Dummy':
    from .dummy.bot import (
        get_bot, find_handler,
        handle_message,
        start,
        register_command_handler,
        register_message_handler
    )
    from .dummy import actions
elif BOT_TYPE == 'pyTelegramBotAPI':  # pragma: no cover
    from .py_telegram_bot_api.bot import (
        get_bot, find_handler,
        handle_message,
        start,
        register_command_handler,
        register_message_handler
    )
    from .py_telegram_bot_api import actions

from . import links
