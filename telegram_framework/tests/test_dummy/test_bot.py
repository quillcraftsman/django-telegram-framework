from django.test import SimpleTestCase
from telegram_framework.dummy import bots
from telegram_framework import messages


class TestDummyBot(SimpleTestCase):

    def setUp(self):
        self.bot = bots.DummyBot(token='test_dummy')

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
        bot = bots.register_command_handler(self.bot, self.some_handler, 'some_handler')
        self.assertEqual(1, len(bot.command_handlers))
        self.assertEqual(self.some_handler, bot.command_handlers['some_handler'])

    def test_register_message_handler(self):
        """
        Test register_message_handler
        """
        bot = bots.register_message_handler(self.bot, self.some_handler)
        self.assertEqual(1, len(bot.message_handlers))
        self.assertEqual(self.some_handler, bot.message_handlers[0])

    def test_register_call_handler(self):
        """
        Test register_call_handler: success
        """
        self.assertEqual(0, len(self.bot.call_handlers))
        bot = bots.register_call_handler(self.bot, self.some_handler, 'some_handler')
        self.assertEqual(1, len(bot.call_handlers))
        self.assertEqual(self.some_handler, bot.call_handlers['some_handler'])

    def test_get_bot(self):
        """
        Test get_bot: success
        """
        bot = bots.get_bot('some_token')
        self.assertTrue(isinstance(bot, bots.DummyBot))

    def test_find_handler_command(self):
        """
        Test find_handler: success: command found
        """
        bot = bots.register_command_handler(self.bot, self.some_handler, 'some_handler')
        message = messages.Message(text='/some_handler', sender='some_sender')
        handler = bots.find_handler(bot, message)
        self.assertEqual(handler, self.some_handler)

    def test_find_handler_command_none(self):
        """
        Test find_handler: success: no command
        """
        message = messages.Message(text='/some_handler', sender='some_sender')
        handler = bots.find_handler(self.bot, message)
        self.assertIsNone(handler)

    def test_find_handler_message(self):
        """
        Test find_handler: success: message
        """
        bot = bots.register_message_handler(self.bot, self.some_handler)
        message = messages.Message(text='some message', sender='some_sender')
        handler = bots.find_handler(bot, message)
        self.assertEqual(self.some_handler, handler)

    def test_find_handler_message_none(self):
        """
        Test find_handler: success: no message
        """
        message = messages.Message(text='some message', sender='some_sender')
        handler = bots.find_handler(self.bot, message)
        self.assertIsNone(handler)

    def test_start(self):
        bots.start(self.bot)
