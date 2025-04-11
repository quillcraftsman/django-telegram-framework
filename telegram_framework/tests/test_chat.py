"""
Tests
"""
from dataclasses import dataclass
from telegram_framework.test import SimpleTestCase
from telegram_framework import chats, messages


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
        self.chat = chats.Chat()


    def test_add_bot(self):
        """
        Test add_bot: success
        """
        bot = EmptyBot()
        self.assertEqual(0, len(self.chat.bots))
        chat = chats.add_bot(self.chat, bot)
        self.assertEqual(1, len(chat.bots))
        chat_bot = chat.bots[0]
        self.assertEqual(bot, chat_bot)

    def test_add_message(self):
        """
        Test add_message: success
        """
        self.assertEmptyChat(self.chat)
        message = messages.Message(text='some text', sender='some sender')
        chat = chats.add_message(self.chat, message)
        self.assertNotEmptyChat(chat)

    def test_add_message_in_chat(self):
        """
        Test add_message: success: Message.chat is not None
        """
        message = messages.Message(text='some text', sender='some sender')
        chat = chats.add_message(self.chat, message)
        chat_message = chats.get_last_message(chat)
        self.assertChatLastMessageEqual(chat, chat_message)
        self.assertEqual(chat, chat_message.chat)

    def test_get_last_message_empty(self):
        """
        Test get_last_message: success: from empty chat
        """
        message = chats.get_last_message(self.chat)
        self.assertIsNone(message)

    def test_get_last_message(self):
        """
        Test get_last_message: success
        """
        message = messages.Message(text='some text', sender='some sender')
        chat = chats.add_message(self.chat, message)
        self.assertEqual(1, len(chat.messages))
        last_message = chats.get_last_message(chat)
        self.assertEqual(message, last_message)
        self.assertEqual(last_message.chat, chat)
        self.assertEqual(len(last_message.chat.messages), len(chat.messages))
