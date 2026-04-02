from telegram_framework import chats, bots, messages
from telegram_framework.commands import actions
from telegram_framework.test import asserts


def test_bot_father_commands():
    """
    Test: bot_father_commands: success empty commands list
    """
    chat = chats.Chat()
    bot = bots.get_bot('dummy')
    chat = chats.add_bot(chat, bot)
    message = messages.create_message('/bot_father_commands', bot)
    chat_message = messages.create_chat_message(message, chat)
    chat = actions.bot_father_commands(bot, chat_message)
    asserts.assert_chat_last_message_text_equal(chat, '-')
