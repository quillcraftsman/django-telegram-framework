from datetime import datetime
from django.test import SimpleTestCase
from telegram_framework import messages
from telegram_framework.messages.errors import (
    MessageNotInChatError,
)


class TestErrors(SimpleTestCase):

    def test_message_not_in_chat_error_str(self):
        """
        Test MessageNotInChatError str
        """
        text = 'some text'
        message = messages.Message(
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
        expected_text = (f'Нельзя ответить на сообщение "{text}", '
                         f'потому что оно не находиться в чате')
        self.assertEqual(expected_text, str(MessageNotInChatError(message)))
