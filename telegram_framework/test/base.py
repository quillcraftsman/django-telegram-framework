from telegram_framework import chats


# pylint: disable=invalid-name
class TelegramFrameworkMixin:

    def assertEmptyChat(self, chat: chats.Chat):
        self.assertFalse(chat.messages)

    def assertNotEmptyChat(self, chat: chats.Chat):
        self.assertTrue(chat.messages)

    def assertChatMessagesCount(self, chat: chats.Chat, count: int):
        self.assertEqual(len(chat.messages), count)

    def assertChatLastMessageEqual(self, chat: chats.Chat, message):
        self.assertEqual(chats.get_last_message(chat), message)

    def assertChatLastMessageTextEqual(self, chat: chats.Chat, text):
        self.assertEqual(chats.get_last_message(chat).text, text)
