from django.test import SimpleTestCase
from telegram_framework.python_telegram_bot import bots

class TestPTB(SimpleTestCase):

    def setUp(self):
        self.bot = bots.get_bot('7777777777:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

        def some_handler():
            return 'data'

        self.some_handler = some_handler

    def test_some_handler(self):
        self.assertEqual('data', self.some_handler())
    def test_get_bot(self):
        self.assertIsInstance(self.bot, bots.Updater)

    def test_start(self):
        class MockedBot:

            def __init__(self):
                self.start_polling_call_count = 0
                self.idle_call_count = 0

            def start_polling(self):
                self.start_polling_call_count += 1

            def idle(self):
                self.idle_call_count += 1

        bot = MockedBot()
        bots.start(bot)
        self.assertEqual(1, bot.start_polling_call_count)
        self.assertEqual(1, bot.idle_call_count)

    def test_register_command_handler(self):
        """
        Test register_command_handler: success
        """
        dispatcher = self.bot.dispatcher
        self.assertEqual(0, len(dispatcher.handlers))
        bot = bots.register_command_handler(self.bot, self.some_handler, 'some_handler')
        dispatcher = bot.dispatcher
        self.assertEqual(1, len(dispatcher.handlers))

    def test_register_text_handler(self):
        """
        Test register_text_handler: success
        """
        dispatcher = self.bot.dispatcher
        self.assertEqual(0, len(dispatcher.handlers))
        bot = bots.register_text_handler(self.bot, self.some_handler, 'some_handler')
        dispatcher = bot.dispatcher
        self.assertEqual(0, len(dispatcher.handlers))

    def test_register_call_handler(self):
        """
        Test register_call_handler: success
        """
        dispatcher = self.bot.dispatcher
        self.assertEqual(0, len(dispatcher.handlers))
        bot = bots.register_call_handler(self.bot, self.some_handler, 'some_handler')
        dispatcher = bot.dispatcher
        self.assertEqual(0, len(dispatcher.handlers))

    def test_register_message_handler(self):
        """
        Test register_message_handler: success
        """
        dispatcher = self.bot.dispatcher
        self.assertEqual(0, len(dispatcher.handlers))
        bot = bots.register_message_handler(self.bot, self.some_handler, 'some_handler')
        dispatcher = bot.dispatcher
        self.assertEqual(0, len(dispatcher.handlers))
