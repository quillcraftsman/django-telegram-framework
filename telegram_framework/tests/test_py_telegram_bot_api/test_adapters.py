import unittest
from telebot import types
from telegram_framework import messages, chats
from telegram_framework.py_telegram_bot_api import adapters, bots


class TestAdapters(unittest.TestCase):

    def setUp(self):
        self.bot = bots.get_bot('7777777777:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

    def test_prepare_handler(self):

        current_chat = chats.Chat(id=0)

        def handler_function(bot, message):  # pylint: disable=unused-argument
            return current_chat

        prepared_function = adapters.prepare_handler(handler_function, self.bot)

        message = messages.create_message(
            'some message',
            sender='bot',
            message_id=1,
        )

        chat_message = messages.create_chat_message(
            message,
            current_chat
        )

        result = prepared_function(chat_message)
        self.assertEqual(current_chat, result)

    def test_prepare_call_handler(self):

        current_chat = chats.Chat(id=0)

        def handler_function(bot, call):  # pylint: disable=unused-argument
            return current_chat

        prepared_function = adapters.prepare_call_handler(handler_function, self.bot)

        class MockCall:

            def __init__(self):
                self.message = None

        call = MockCall()
        result = prepared_function(call)
        self.assertEqual(current_chat, result)

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
        class FromUser:

            def __init__(self):
                self.id = 1
                self.first_name = 'test'
                self.last_name = 'test'
                self.username = 'test'


        telebot_message = types.Message(
            1,
            FromUser(),
            'date',
            chat=types.Chat(id=1, type=0),
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
                self.chat = chats.Chat(0)
                self.message_id = 640

        telebot_message = types.CallbackQuery(
            1,
            1,
            'data',
            chats.Chat,
            'date',
            TelebotMockMessage(),
            None,
            None,
        )
        message = adapters.prepare_message(telebot_message)
        self.assertEqual('data', message.data)
