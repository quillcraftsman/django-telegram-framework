from django.test import SimpleTestCase
from telegram_framework import get_bot, links, actions
from telegram_framework.chat import Chat, add_bot, get_messages
from telegram_framework.messages import Message
from demo.links import bot_links


class TestIntegration(SimpleTestCase):

    def setUp(self):
        chat = Chat()
        self.client = get_bot('client_token')
        chat = add_bot(chat, self.client)
        bot = get_bot('bot')
        bot = links.add_links(bot, bot_links)
        self.chat = add_bot(chat, bot)

    def test_say_hello(self):

        client_message = Message(text='/hello', sender=self.client)
        chat = actions.send_message(self.chat, client_message)
        self.assertEqual(2, len(chat.messages))
        messages = get_messages(chat)
        self.assertEqual(messages[0].text, '/hello')
        self.assertEqual(messages[1].text, 'hello')

    def test_send_hello_as_reply(self):

        client_message = Message(text='/reply_me', sender=self.client)
        chat = actions.send_message(self.chat, client_message)
        self.assertEqual(2, len(chat.messages))
        messages = get_messages(chat)
        self.assertEqual(messages[0].text, '/reply_me')
        self.assertEqual(messages[1].text, 'hello')
