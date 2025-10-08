from django.test import SimpleTestCase
from telegram_framework.dummy import bots
from telegram_framework import messages


class TestDummyBot(SimpleTestCase):

    def setUp(self):
        self.bot = bots.get_bot(token='test_dummy')

        def some_handler():
            return 'data'

        self.some_handler = some_handler

    def test_some_handler_call(self):
        self.assertEqual('data', self.some_handler())

    # def test_register_command_handler(self):
    #     """
    #     Test register_command_handler: success
    #     """
    #     self.assertEqual(0, len(self.bot.command_handlers))
    #     bot = bots.register_command_handler(self.bot, self.some_handler, 'some_handler')
    #     self.assertEqual(1, len(bot.command_handlers))
    #     self.assertEqual(self.some_handler, bot.command_handlers['some_handler'].function)

    def test_register_message_handler(self):
        """
        Test register_message_handler: success
        """
        bot = bots.register_message_handler(self.bot, self.some_handler)
        self.assertEqual(1, len(bot.message_handlers))
        registered_handler = bot.message_handlers[0]
        self.assertEqual(self.some_handler, registered_handler.function)
        self.assertIsNotNone(registered_handler.filter)

    def test_register_message_handler_filter(self):
        """
        Test register_message_handler with filter: success
        """
        def filter_function(message):  # pylint:disable=unused-argument
            return False

        bot = bots.register_message_handler(self.bot, self.some_handler, filter_function)
        self.assertEqual(1, len(bot.message_handlers))
        registered_handler = bot.message_handlers[0]
        self.assertEqual(self.some_handler, registered_handler.function)
        self.assertEqual(filter_function, registered_handler.filter)
        self.assertFalse(registered_handler.filter(None))

    def test_register_text_handler(self):
        """
        Test register_text_handler: success
        """
        bot = bots.register_text_handler(self.bot, self.some_handler, 'fixed text')
        self.assertEqual(1, len(bot.message_handlers))

    def test_register_call_handler(self):
        """
        Test register_call_handler: success
        """
        self.assertEqual(0, len(self.bot.call_handlers))
        bot = bots.register_call_handler(self.bot, self.some_handler, 'some_handler')
        self.assertEqual(1, len(bot.call_handlers))
        self.assertEqual(self.some_handler, bot.call_handlers['some_handler'].function)

    def test_get_bot(self):
        """
        Test get_bot: success
        """
        bot = bots.get_bot('some_token')
        self.assertTrue(isinstance(bot, bots.DummyBot))

    # def test_find_handler_command(self):
    #     """
    #     Test find_handler: success: command found
    #     """
    #     bot = bots.register_command_handler(self.bot, self.some_handler, 'some_handler')
    #     message = messages.Message(text='/some_handler', sender='some_sender')
    #     handler = bots.find_handler(bot, message)
    #     self.assertEqual(self.some_handler, handler.function)

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
        self.assertEqual(self.some_handler, handler.function)

    def test_find_handler_message_none(self):
        """
        Test find_handler: success: no message
        """
        message = messages.Message(text='some message', sender='some_sender')
        handler = bots.find_handler(self.bot, message)
        self.assertIsNone(handler)

    def test_start(self):
        bots.start(self.bot)

    # def test_get_commands_list(self):
    #     """
    #     Test get_commands_list: success
    #     """
    #     self.assertEqual([], bots.get_commands_list(self.bot))
    #     handler_name = 'some_handler'
    #     bot = bots.register_command_handler(self.bot, self.some_handler, handler_name)
    #     self.assertEqual([(handler_name, self.some_handler)], bots.get_commands_list(bot))
