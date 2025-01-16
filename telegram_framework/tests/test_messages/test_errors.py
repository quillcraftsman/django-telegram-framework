from datetime import datetime
from django.test import SimpleTestCase
from telegram_framework.messages import Message
from telegram_framework.messages.errors import (
    MessageNotInChatError,
)


class TestErrors(SimpleTestCase):

    def test_message_not_in_chat_error_str(self):
        """
        Test MessageNotInChatError str
        """
        message = Message(
            'some text',
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
        expected_text = ("Нельзя ответить на сообщение Message(text='some text', "
                         "sender='some sender', "
                         "timestamp=datetime.datetime(2025, 1, 1, 12, 0), chat=None), "
                         "потому что оно не находиться в чате")
        self.assertEqual(expected_text, str(MessageNotInChatError(message)))
