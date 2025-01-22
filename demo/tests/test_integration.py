from django.test import SimpleTestCase
from telegram_framework import get_bot, links, actions
from telegram_framework.chat import Chat, add_bot, get_messages
from telegram_framework.messages import Message
from demo.links import bot_links


class TestIntegration(SimpleTestCase):

    def test_say_hello(self):
        chat = Chat()
        client = get_bot('client_token')
        chat = add_bot(chat, client)
        bot = get_bot('bot')
        bot = links.add_links(bot, bot_links)
        chat = add_bot(chat, bot)
        client_message = Message(text='/hello', sender=client)
        chat = actions.send_message(chat, client_message)
        self.assertEqual(2, len(chat.messages))
        messages = get_messages(chat)
        self.assertEqual(messages[0].text, '/hello')
        self.assertEqual(messages[1].text, 'hello')