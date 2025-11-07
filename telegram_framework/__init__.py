# pylint: disable=wrong-import-position
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from telegram_framework import errors


try:
    BOT_TYPE = settings.TELEGRAM_BOT_TYPE
except (ImproperlyConfigured, AttributeError):  # pragma: no cover
    BOT_TYPE = 'Dummy'

if BOT_TYPE == 'Dummy':
    from .dummy import bots
    from .dummy import actions
elif BOT_TYPE == 'pyTelegramBotAPI':  # pragma: no cover
    from .py_telegram_bot_api import bots
    from .py_telegram_bot_api import actions
elif BOT_TYPE == 'PYTHON_TELEGRAM_BOT':  # pragma: no cover
    from .python_telegram_bot import bots
    from .python_telegram_bot import actions
else:
    raise errors.BotTypeError(BOT_TYPE)  # pragma: no cover

from . import links
