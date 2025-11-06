# pylint: disable=duplicate-code
from telegram_framework.test import SimpleTestCase
from telegram_framework.python_telegram_bot import actions
from telegram_framework import chats
from telegram_framework import messages


class MockBot:

    def __init__(self, *args, **kwargs):
        pass

    def send_message(self, chat_id, text, parse_mode=None):
        pass


class MockUpdater:

    def __init__(self):
        self.bot = MockBot()


class TestActions(SimpleTestCase):

    def setUp(self):
        self.bot = MockUpdater()

    def test_send_message(self):
        """
        Test send_message: success
        """
        chat = chats.Chat()
        self.assertEqual(0, len(chat.messages))
        message = messages.create_message('new message', sender=self.bot)
        chat = actions.send_message(chat, message)
        self.assertEqual(1, len(chat.messages))
        last_message = chats.get_last_message(chat)
        self.assertEqual(message, last_message)
