# pylint: disable=duplicate-code
from pathlib import Path
from django.test import SimpleTestCase
from telegram_framework.py_telegram_bot_api import actions
from telegram_framework import chats
from telegram_framework import messages, media


class MockTelebot:

    def send_message(self, chat_id, text, parse_mode=None):
        pass

    def reply_to(self, message, text):
        pass

    def send_photo(self, chat_id, photo, caption, parse_mode):
        pass


class TestActions(SimpleTestCase):

    def setUp(self):
        self.bot = MockTelebot()

    def test_send_image(self):
        """
        Test send_image: success
        """
        chat = chats.Chat()
        self.assertEqual(0, len(chat.messages))
        caption_message = messages.create_message('Image caption', sender=self.bot)
        current_dir = Path(__file__).parent
        image_file_path = current_dir / "data" / "empty.jpg"
        message = media.create_image(
            sender=self.bot,
            file_path=image_file_path,
            caption=caption_message
        )
        chat = actions.send_image(chat, message)
        self.assertEqual(1, len(chat.messages))
        last_message = chats.get_last_message(chat)
        # Fix IT
        self.assertEqual(caption_message, last_message)


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


    def test_send_reply(self):
        """
        Test send_reply: failed: message has no chat
        """
        chat = chats.Chat()
        self.assertEqual(0, len(chat.messages))
        message = messages.create_message('new message', sender=self.bot)
        chat = chats.add_message(chat, message)
        last_message = chats.get_last_message(chat)
        reply = messages.create_reply(last_message, 'reply', sender=self.bot)
        chat = actions.send_reply(reply)
        last_reply = chats.get_last_message(chat)
        expected_reply = messages.create_reply(
            last_message,
            text = 'reply',
            sender=self.bot,
        )
        self.assertEqual(expected_reply, last_reply)
