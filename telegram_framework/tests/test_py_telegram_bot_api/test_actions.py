# pylint: disable=duplicate-code
# pylint: disable=redefined-outer-name
from pathlib import Path
import pytest
from telegram_framework.test import asserts
from telegram_framework.py_telegram_bot_api import actions
from telegram_framework import chats
from telegram_framework import messages, keyboards


class MockTelebot:

    def __init__(self, *args, **kwargs):
        pass

    def send_message(self, chat_id, text, parse_mode=None, reply_markup=None):
        pass

    def reply_to(self, message, text):
        pass

    def send_photo(
            self,
            chat_id,
            photo,
            caption,
            parse_mode=None,
            reply_markup=None
    ):  # pylint:disable=too-many-arguments),too-many-positional-arguments
        pass


@pytest.fixture
def bot():
    return MockTelebot()


def test_send_image(bot):
    """
    Test send_image: success
    """
    chat = chats.Chat()
    assert 0 == len(chat.messages)
    caption_message = messages.create_message(
        'Image caption',
        sender=bot
    )
    current_dir = Path(__file__).parent
    image_file_path = current_dir / "data" / "empty.jpg"
    message = messages.create_image(
        sender=bot,
        file_path=image_file_path,
        caption=caption_message
    )
    chat = actions.send_image(chat, message)
    assert 1 == len(chat.messages)
    last_message = chats.get_last_message(chat)
    assert isinstance(last_message, messages.Image)
    assert last_message.caption.text == 'Image caption'
    assert last_message == message


def test_send_message(bot):
    """
    Test send_message: success
    """
    chat = chats.Chat()
    assert 0 == len(chat.messages)
    message = messages.create_message(
        'new message',
        sender=bot
    )
    keyboard = keyboards.inline.Keyboard(
        buttons=[keyboards.inline.Button('Some button', 'some_data')]
    )
    message = messages.add_keyboard(message, keyboard)
    chat = actions.send_message(chat, message)
    assert 1 == len(chat.messages)
    last_message = chats.get_last_message(chat)
    assert message == last_message


def test_send_message_force_reply_keyboard(bot):
    """
    Test send_message with force.keyboard: success
    """
    chat = chats.Chat()
    assert 0 == len(chat.messages)
    message = messages.create_message(
        'new message',
        sender=bot
    )
    keyboard = keyboards.force.Keyboard()
    message = messages.add_keyboard(message, keyboard)
    chat = actions.send_message(chat, message)
    assert 1 == len(chat.messages)
    last_message = chats.get_last_message(chat)
    assert message == last_message
    asserts.assert_keyboard_in_message(last_message)


def test_send_message_with_reply_keyboard(bot):
    """
    Test send_message with reply.keyboard success
    """
    chat = chats.Chat()
    message = messages.create_message(
        'new message',
        sender=bot
    )
    keyboard = keyboards.reply.Keyboard(
        'Test keyboard',
        buttons=[keyboards.reply.Button('Some button')],
    )
    message = messages.add_keyboard(message, keyboard)
    asserts.assert_keyboard_not_in_chat(chat)
    chat = actions.send_message(chat, message)
    asserts.assert_keyboard_in_message(chat)

    message = messages.create_message('new message', sender=bot)
    keyboard = keyboards.reply.EmptyKeyboard(
    )
    message = messages.add_keyboard(message, keyboard)
    chat = actions.send_message(chat, message)
    asserts.assert_keyboard_not_in_chat(chat)


def test_send_reply(bot):
    """
    Test send_reply: failed: message has no chat
    """
    chat = chats.Chat()
    assert 0 == len(chat.messages)
    message = messages.create_message(
        'new message',
        sender=bot
    )
    chat = chats.add_message(chat, message)
    last_message = chats.get_last_message(chat)
    reply = messages.create_reply(
        last_message,
        'reply',
        sender=bot
    )
    chat = actions.send_reply(reply)
    last_reply = chats.get_last_message(chat)
    expected_reply = messages.create_reply(
        last_message,
        text = 'reply',
        sender=bot,
    )
    assert expected_reply == last_reply
