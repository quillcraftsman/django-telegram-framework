from django.test import SimpleTestCase
from telegram_framework.dummy.bot import (
    DummyBot,
    register_command_handler,
    register_message_handler,
    register_call_handler,
)


class TestDummyBot(SimpleTestCase):

    def setUp(self):
        self.bot = DummyBot(token='test_dummy')

        def some_handler():
            return 'data'

        self.some_handler = some_handler

    def test_some_handler_call(self):
        self.assertEqual('data', self.some_handler())

    def test_register_command_handler(self):
        """
        Test register_command_handler: success
        """
        self.assertEqual(0, len(self.bot.command_handlers))
        bot = register_command_handler(self.bot, self.some_handler, 'some_handler')
        self.assertEqual(1, len(bot.command_handlers))
        self.assertEqual(self.some_handler, bot.command_handlers['some_handler'])

    def test_register_message_handler(self):
        """
        Test register_message_handler
        """
        bot = register_message_handler(self.bot, self.some_handler)
        self.assertEqual(1, len(bot.message_handlers))
        self.assertEqual(self.some_handler, bot.message_handlers[0])

    def test_register_call_handler(self):
        """
        Test register_call_handler: success
        """
        self.assertEqual(0, len(self.bot.call_handlers))
        bot = register_call_handler(self.bot, self.some_handler, 'some_handler')
        self.assertEqual(1, len(bot.call_handlers))
        self.assertEqual(self.some_handler, bot.call_handlers['some_handler'])
