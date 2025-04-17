from telegram_framework import chats, bots, messages
from telegram_framework.commands import actions
from telegram_framework.test import SimpleTestCase


class TestActions(SimpleTestCase):

    def test_get_commands(self):
        """
        Test: get_commands: success empty commands list
        """
        chat = chats.Chat()
        bot = bots.get_bot('dummy')
        chat = chats.add_bot(chat, bot)
        message = messages.create_message('/commands', bot)
        chat_message = messages.create_chat_message(message, chat)
        chat = actions.get_commands(bot, chat_message)
        self.assertChatLastMessageTextEqual(chat, '-')
