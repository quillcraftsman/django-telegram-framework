import unittest
from telegram_framework.py_telegram_bot_api import adapters, bots


class TestAdapters(unittest.TestCase):

    def setUp(self):
        self.bot = bots.get_bot('7777777777:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

    def test_prepare_handler(self):

        def handler_function(bot):  # pylint: disable=unused-argument
            return 'result'

        prepared_function = adapters.prepare_handler(handler_function, self.bot)
        result = prepared_function()
        self.assertEqual('result', result)

    def test_prepare_call_handler(self):

        def handler_function(bot, call):  # pylint: disable=unused-argument
            return 'result'

        prepared_function = adapters.prepare_call_handler(handler_function, self.bot)

        class MockCall:

            def __init__(self):
                self.message = None

        call = MockCall()
        result = prepared_function(call)
        self.assertEqual('result', result)
