from django.test import SimpleTestCase
from telegram_framework.py_telegram_bot_api import bots
from telegram_framework.messages import Message


class TestTeleBot(SimpleTestCase):

    def setUp(self):
        self.bot = bots.get_bot('7777777777:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

        def some_handler():
            return 'data'

        self.some_handler = some_handler

    def test_some_handler_call(self):
        self.assertEqual('data', self.some_handler())

    def test_register_command_handler(self):
        """
        Test register_command_handler: success
        """
        self.assertEqual(0, len(self.bot.message_handlers))
        bot = bots.register_command_handler(self.bot, self.some_handler, 'some_handler')
        self.assertEqual(1, len(bot.message_handlers))

    def test_register_message_handler(self):
        """
        Test register_message_handler
        """
        bot = bots.register_message_handler(self.bot, self.some_handler)
        self.assertEqual(1, len(bot.message_handlers))

    def test_register_call_handler(self):
        """
        Test register_call_handler: success
        """
        self.assertEqual(0, len(self.bot.callback_query_handlers))
        bot = bots.register_call_handler(self.bot, self.some_handler, 'some_handler')
        self.assertEqual(1, len(bot.callback_query_handlers))

    def test_get_bot(self):
        """
        Test get_bot: success
        """
        self.assertTrue(isinstance(self.bot, bots.TeleBot))

    def test_find_handler(self):
        """
        Test find_handler: success
        """
        message = Message(text='some message', sender='some_sender')
        # handler = find_handler(self.bot, message)
        self.assertIsNone(bots.find_handler(self.bot, message))

    def test_handle_message(self):
        """
        Test handle_message success
        """
        class MockMessage:

            def __init__(self):
                self.chat = 'some chat'

        message = MockMessage()
        chat = bots.handle_message(self.bot, message)
        self.assertEqual(chat, message.chat)

    def test_prepare_handler(self):

        def handler_function(bot):  # pylint: disable=unused-argument
            return 'result'

        prepared_function = bots.prepare_handler(handler_function, self.bot)
        result = prepared_function()
        self.assertEqual('result', result)

    def test_start(self):

        class MockedBot:

            def __init__(self):
                self.infinity_polling_call_count = 0

            def infinity_polling(self):
                self.infinity_polling_call_count += 1

        bot = MockedBot()
        bots.start(bot)
        self.assertEqual(1, bot.infinity_polling_call_count)
