from telegram_framework import chats
from telegram_framework.test import SimpleTestCase


class TestCommands(SimpleTestCase):  # pylint: disable=too-many-public-methods
    ROOT_BOT_LINKS = 'demo.links'

    def test_start(self):
        """
        Test /start: success
        """
        chat = self.assertCommandWasHandled('/start', self.chat)
        last_message = chats.get_last_message(chat)
        expected_text = 'Привет, Я Demo Bot'
        self.assertIn(expected_text, last_message.text)


    def test_help(self):
        """
        Test /help: success
        """
        chat = self.assertCommandWasHandled('/help', self.chat)
        last_message = chats.get_last_message(chat)
        expected_text = 'Привет, Я Demo Bot'
        self.assertIn(expected_text, last_message.text)


    def test_bot_father_commands(self):
        """
        Test /bot_father_commands: success
        """
        chat = self.assertCommandWasHandled('/bot_father_commands', self.chat)
        last_message = chats.get_last_message(chat)
        expected_text = 'commands'
        self.assertIn(expected_text, last_message.text)

    def test_commands(self):
        """
        Test /commands: success
        """
        chat = self.assertCommandWasHandled('/commands', self.chat)
        last_message = chats.get_last_message(chat)
        expected_text = 'commands'
        self.assertIn(expected_text, last_message.text)
