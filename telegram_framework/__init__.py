# pylint: disable=wrong-import-position
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

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

from . import links
