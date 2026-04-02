from datetime import datetime
from telegram_framework.messages.text_message import Message


def test_str():
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
    assert text == str(message)
