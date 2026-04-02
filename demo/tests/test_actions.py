from telegram_framework import chats
from telegram_framework.test import asserts


def test_start(bot_client, chat):
    """
    Test /start: success
    """
    chat = asserts.assert_command_was_handled('/start', chat, bot_client)
    last_message = chats.get_last_message(chat)
    expected_text = 'Привет, Я Demo Bot'
    assert expected_text in last_message.text


def test_help(bot_client, chat):
    """
    Test /help: success
    """
    chat = asserts.assert_command_was_handled('/help', chat, bot_client)

    last_message = chats.get_last_message(chat)
    expected_text = 'Привет, Я Demo Bot'
    assert expected_text in last_message.text


def test_bot_father_commands(bot_client, chat):
    """
    Test /bot_father_commands: success
    """
    chat = asserts.assert_command_was_handled(
        '/bot_father_commands',
        chat,
        bot_client,
    )
    last_message = chats.get_last_message(chat)
    expected_text = 'commands'
    assert expected_text in last_message.text


def test_commands(bot_client, chat):
    """
    Test /commands: success
    """
    chat = asserts.assert_command_was_handled(
        '/commands',
        chat,
        bot_client,
    )
    last_message = chats.get_last_message(chat)
    expected_text = 'commands'
    assert expected_text in last_message.text
