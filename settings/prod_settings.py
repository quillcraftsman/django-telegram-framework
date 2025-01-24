# pragma: no cover
from os import getenv
from dotenv import load_dotenv
from .settings import *  # pylint: disable=wildcard-import,unused-wildcard-import

load_dotenv()

TELEGRAM_BOT_TOKEN = getenv('TELEGRAM_BOT_TOKEN', '0')
TELEGRAM_BOT_TYPE = getenv('TELEGRAM_BOT_TYPE', 'Dummy')
