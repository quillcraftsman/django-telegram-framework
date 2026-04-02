from datetime import datetime
from telegram_framework import messages
from telegram_framework.messages.errors import (
    MessageNotInChatError,
)


def test_message_not_in_chat_error_str():
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
    assert expected_text == str(MessageNotInChatError(message))
