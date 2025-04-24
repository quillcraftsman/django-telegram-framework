from datetime import datetime
import unittest
from telegram_framework.messages.text_message import Message


class TestMessage(unittest.TestCase):

    def test_str(self):
        text = 'some text'
        message = Message(
            text='some text',
            sender='some sender',
            timestamp=datetime(
                2025,
                1,
                1,
                12,
                0,
                0,
                0)
        )
        self.assertEqual(text, str(message))
