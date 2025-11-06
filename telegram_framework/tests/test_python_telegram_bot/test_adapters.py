import unittest
from telegram_framework import chats
from telegram_framework.python_telegram_bot import adapters, bots


class TestAdapters(unittest.TestCase):

    def setUp(self):
        self.bot = bots.get_bot('7777777777:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

    def test_prepare_handler(self):

        current_chat = chats.Chat(id=0)

        def handler_function(bot, message):  # pylint: disable=unused-argument
            return current_chat

        prepared_function = adapters.prepare_handler(handler_function, self.bot)

        class MockUser:

            def __init__(self):
                self.id = '123456'
                self.first_name = 'Mock'
                self.last_name = 'Mock'
                self.username = 'Mock'

        class MockChat:

            def __init__(self):
                self.id = 0

        class MockMessage:

            def __init__(self):
                self.from_user = MockUser()
                self.text = 'mock text'
                self.reply_markup = None
                self.message_id = 0
                self.chat = MockChat()

        class MockUpdate:

            def __init__(self):
                self.message = MockMessage()

        prepared_function(MockUpdate(), None)
