import unittest
from telebot import types
from telegram_framework.py_telegram_bot_api import adapters, bots


class TestAdapters(unittest.TestCase):

    def setUp(self):
        self.bot = bots.get_bot('7777777777:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

    def test_prepare_handler(self):

        def handler_function(bot, message):  # pylint: disable=unused-argument
            return 'result'

        prepared_function = adapters.prepare_handler(handler_function, self.bot)
        result = prepared_function('some message')
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

    def test_prepare_message(self):

        class MockUser:

            def __init__(self):
                self.id = '0'

        text =  'telebot message'
        class TelebotMockMessage(types.Message):

            def __init__(self):  # pylint: disable=(super-init-not-called
                self.text = 'telebot message'
                self.from_user = MockUser()
                self.reply_markup = 'HTML'
                self.chat = 'some chat'

        message = adapters.prepare_message(TelebotMockMessage())
        self.assertEqual(text, message.text)
