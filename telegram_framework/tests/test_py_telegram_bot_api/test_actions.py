# pylint: disable=duplicate-code
from django.test import SimpleTestCase
from telegram_framework.py_telegram_bot_api.actions import send_message, send_reply
from telegram_framework import chats
from telegram_framework import messages


class MockTelebot:

    def send_message(self, chat_id, text):
        pass

    def reply_to(self, message, text):
        pass


class TestActions(SimpleTestCase):

    def setUp(self):
        self.bot = MockTelebot()

    def test_send_message(self):
        """
        Test send_message: success
        """
        chat = chats.Chat()
        self.assertEqual(0, len(chat.messages))
        message = messages.Message('new message', sender=self.bot)
        chat = send_message(chat, message)
        self.assertEqual(1, len(chat.messages))
        last_message = chats.get_last_message(chat)
        self.assertEqual(message, last_message)

    def test_send_reply(self):
        """
        Test send_reply: failed: message has no chat
        """
        chat = chats.Chat()
        self.assertEqual(0, len(chat.messages))
        message = messages.Message('new message', sender=self.bot)
        chat = chats.add_message(chat, message)
        last_message = chats.get_last_message(chat)
        reply = messages.create_reply(last_message, 'reply', sender=self.bot)
        chat = send_reply(reply)
        last_reply = chats.get_last_message(chat)
        # expected_reply = Reply(
        #     'reply',
        #     self.bot,
        #     message=last_message,
        #     chat=last_message.chat
        # )
        expected_reply = messages.create_reply(
            last_message,
            text = 'reply',
            sender=self.bot,
        )
        self.assertEqual(expected_reply, last_reply)
