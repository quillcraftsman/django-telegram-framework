from django.test import SimpleTestCase
from telegram_framework import get_bot
from telegram_framework import actions
from telegram_framework.chat import Chat, add_bot, get_last_message
from telegram_framework.links import add_links
from telegram_framework import messages
from demo.links import bot_links
from demo.models import create_info_text


class TestCommands(SimpleTestCase):

    def setUp(self):
        chat = Chat()
        self.client = get_bot('client')
        chat = add_bot(chat, self.client)
        bot = get_bot('bot')
        bot = add_links(bot, bot_links)
        self.chat = add_bot(chat, bot)
        self.assertEqual(0, len(self.chat.messages))

    def test_start(self):
        """
        Test /start: success
        """
        command_text = '/start'
        message = messages.Message(command_text, sender=self.client)
        chat = actions.send_message(self.chat, message)
        self.assertEqual(2, len(chat.messages))
        last_message = get_last_message(chat)
        expected_text = create_info_text(command_text)
        self.assertEqual(expected_text, last_message.text)


    def test_help(self):
        """
        Test /help: success
        """
        command_text = '/help'
        message = messages.Message(command_text, sender=self.client)
        chat = actions.send_message(self.chat, message)
        self.assertEqual(2, len(chat.messages))
        last_message = get_last_message(chat)
        expected_text = create_info_text(command_text)
        self.assertEqual(expected_text, last_message.text)


    def test_any_text_message(self):
        """
        Test send any text message: success
        """
        text = 'any message'
        message = messages.Message('any message', sender=self.client)
        chat = actions.send_message(self.chat, message)
        self.assertEqual(2, len(chat.messages))
        last_message = get_last_message(chat)
        expected_text = f'На любое неизвестное сообщение я умею присылать его в ответ: {text}'
        self.assertEqual(expected_text, last_message.text)
