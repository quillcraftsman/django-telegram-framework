# pylint: disable=redefined-outer-name
"""
Tests
"""
from dataclasses import dataclass
import pytest
from telegram_framework.test import asserts
from telegram_framework import chats, messages


@dataclass(frozen=True)
class EmptyBot:
    id: int = 0

    def __eq__(self, other):
        return self.id == other.id


@pytest.fixture
def current_chat():
    return chats.Chat()


def test_add_bot(current_chat):
    """
    Test add_bot: success
    """
    chat = current_chat
    bot = EmptyBot()
    assert 0 == len(chat.bots)
    chat = chats.add_bot(chat, bot)
    assert 1, len(chat.bots)
    chat_bot = chat.bots[0]
    assert bot == chat_bot


def test_add_message(current_chat):
    """
    Test add_message: success
    """
    chat = current_chat
    asserts.assert_empty_chat(chat)
    message = messages.Message(text='some text', sender='some sender')
    chat = chats.add_message(chat, message)
    asserts.assert_not_empty_chat(chat)


def test_add_message_in_chat(current_chat):
    """
    Test add_message: success: Message.chat is not None
    """
    chat = current_chat
    message = messages.Message(text='some text', sender='some sender')
    chat = chats.add_message(chat, message)
    chat_message = chats.get_last_message(chat)
    asserts.assert_chat_last_message_equal(chat, chat_message)
    assert chat == chat_message.chat


def test_get_last_message_empty(current_chat):
    """
    Test get_last_message: success: from empty chat
    """
    chat = current_chat
    message = chats.get_last_message(chat)
    assert message is None


def test_get_last_message(current_chat):
    """
    Test get_last_message: success
    """
    chat = current_chat
    message = messages.Message(text='some text', sender='some sender')
    chat = chats.add_message(chat, message)
    assert 1 == len(chat.messages)
    last_message = chats.get_last_message(chat)
    assert message == last_message
    assert last_message.chat == chat
    assert len(last_message.chat.messages) == len(chat.messages)
