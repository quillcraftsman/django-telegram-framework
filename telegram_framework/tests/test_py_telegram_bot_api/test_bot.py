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

    def test_register_text_handler(self):
        """
        Test register_text_handler
        """
        bot = bots.register_text_handler(self.bot, self.some_handler, 'text')
        self.assertEqual(1, len(bot.message_handlers))

    def test_register_call_handler(self):
        """
        Test register_call_handler: success
        """
        self.assertEqual(0, len(self.bot.callback_query_handlers))
        bot = bots.register_call_handler(self.bot, self.some_handler, 'some_handler')
        self.assertEqual(1, len(bot.callback_query_handlers))

    def test_register_next_step_handler(self):
        """
        Test register_next_step_handler: success
        """
        self.assertEqual(0, len(self.bot.next_step_backend.handlers))

        class MockChat:

            def __init__(self):
                self.id = 1

        chat = bots.register_next_step_handler(self.bot, MockChat(), self.some_handler)
        self.assertEqual(1, chat.id)
        self.assertEqual(1, len(self.bot.next_step_backend.handlers))

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

    def test_start(self):

        class MockedBot:

            def __init__(self):
                self.infinity_polling_call_count = 0

            def infinity_polling(self):
                self.infinity_polling_call_count += 1

        bot = MockedBot()
        bots.start(bot)
        self.assertEqual(1, bot.infinity_polling_call_count)

    def test_get_commands_list(self):
        """
        Test get_commands_list: success
        """
        self.assertEqual([], bots.get_commands_list(self.bot))
        handler_name = 'some_handler'
        bot = bots.register_command_handler(self.bot, self.some_handler, handler_name)
        commands_list = bots.get_commands_list(bot)
        self.assertEqual(1, len(commands_list))
        name, _ = commands_list[0]
        self.assertEqual(handler_name, name)
