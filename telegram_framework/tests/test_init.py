from telebot import TeleBot
from django.test import SimpleTestCase, override_settings


class TestInit(SimpleTestCase):

    @override_settings(TELEGRAM_BOT_TYPE="pyTelegramBotAPI")
    def test_py_telegram_bot_api(self):
        from telegram_framework import get_bot  # pylint: disable=import-outside-toplevel
        bot = get_bot('7777777777:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('TYPE', type(bot))
        self.assertTrue(isinstance(bot, TeleBot))
