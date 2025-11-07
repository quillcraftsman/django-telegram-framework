from django.test import SimpleTestCase
from telegram_framework import errors


class TestErrors(SimpleTestCase):

    def test_bot_type_error_str(self):
        error = errors.BotTypeError('SOME_TYPE')
        self.assertEqual(str(error), 'Unknown BOT_TYPE: SOME_TYPE')
