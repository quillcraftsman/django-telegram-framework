"""
Tests
"""
from dataclasses import dataclass
from django.test import SimpleTestCase
from telegram_framework.chat import Chat, add_bot, get_last_message, add_message
from telegram_framework.messages import Message


@dataclass(frozen=True)
class EmptyBot:
    id: int = 0

    def __eq__(self, other):
        return self.id == other.id


class TestChat(SimpleTestCase):
    """
    TestInfo TestCase
    """
    def setUp(self):
        """
        setUp test data
        """
        self.chat = Chat()


    def test_add_bot(self):
        """
        Test add_bot: success
        """
        bot = EmptyBot()
        self.assertEqual(0, len(self.chat.bots))
        chat = add_bot(self.chat, bot)
        self.assertEqual(1, len(chat.bots))
        chat_bot = chat.bots[0]
        self.assertEqual(bot, chat_bot)

    def test_add_message(self):
        """
        Test add_message: success
        """
        self.assertEqual(0, len(self.chat.messages))
        message = Message(text='some text', sender='some sender')
        chat = add_message(self.chat, message)
        self.assertEqual(1, len(chat.messages))

    def test_add_message_in_chat(self):
        """
        Test add_message: success: Message.chat is not None
        """
        message = Message(text='some text', sender='some sender')
        self.assertIsNone(message.chat)
        chat = add_message(self.chat, message)
        chat_message = get_last_message(chat)
        self.assertEqual(message, chat_message)
        self.assertEqual(chat, chat_message.chat)

    def test_get_last_message_empty(self):
        """
        Test get_last_message: success: from empty chat
        """
        message = get_last_message(self.chat)
        self.assertIsNone(message)

    def test_get_last_message(self):
        """
        Test get_last_message: success
        """
        message = Message(text='some text', sender='some sender')
        chat = add_message(self.chat, message)
        self.assertEqual(1, len(chat.messages))
        last_message = get_last_message(chat)
        self.assertEqual(message, last_message)
        self.assertEqual(last_message.chat, chat)
        self.assertEqual(len(last_message.chat.messages), len(chat.messages))
