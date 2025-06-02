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

    def test_prepare_message_mock(self):

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
                self.message_id = 640

        message = adapters.prepare_message(TelebotMockMessage())
        self.assertEqual(text, message.text)

    def test_prepare_message_message(self):
        """
        Test prepare_message: success telebot.Message input
        """
        telebot_message = types.Message(
            1,
            1,
            'date',
            chat='chat',
            content_type=None,
            options=[],
            json_string='date',
        )
        message = adapters.prepare_message(telebot_message)
        self.assertEqual(None, message.text)

    def test_prepare_message_call(self):
        """
        Test prepare_message: success telebot.CallbackQuery input
        """

        class MockUser:

            def __init__(self):
                self.id = '0'

        class TelebotMockMessage(types.Message):

            def __init__(self):  # pylint: disable=(super-init-not-called
                self.text = 'telebot message'
                self.from_user = MockUser()
                self.reply_markup = 'HTML'
                self.chat = 'some chat'
                self.message_id = 640

        telebot_message = types.CallbackQuery(
            1,
            1,
            'data',
            'chat',
            'date',
            TelebotMockMessage(),
            None,
            None,
        )
        message = adapters.prepare_message(telebot_message)
        self.assertEqual('data', message.data)
