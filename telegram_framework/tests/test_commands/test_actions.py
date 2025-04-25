from telegram_framework import chats, bots, messages
from telegram_framework.commands import actions
from telegram_framework.test import SimpleTestCase


class TestActions(SimpleTestCase):

    def test_bot_father_commands(self):
        """
        Test: bot_father_commands: success empty commands list
        """
        chat = chats.Chat()
        bot = bots.get_bot('dummy')
        chat = chats.add_bot(chat, bot)
        message = messages.create_message('/bot_father_commands', bot)
        chat_message = messages.create_chat_message(message, chat)
        chat = actions.bot_father_commands(bot, chat_message)
        self.assertChatLastMessageTextEqual(chat, '-')
