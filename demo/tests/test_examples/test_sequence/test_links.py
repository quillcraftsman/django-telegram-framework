import pytest
from telegram_framework import chats
from telegram_framework.test import asserts


# START test_sequence_example
@pytest.mark.parametrize('command', [
    '/sequence_example',
    '/sequence_form_example',
])
def test_sequence_example(bot_client, chat, command):
    """
    Test /sequence_example
    """
    chat = asserts.assert_command_was_handled(
        command,
        chat,
        bot_client,
    )
    last_message = asserts.assert_chat_last_message_text_equal(
        chat,
        'Как бы вас звали на букву "Л"?:',
    )
    asserts.assert_keyboard_in_message(last_message)

    chat = asserts.assert_text_message_was_handled(
        'Жук',
        chat,
        bot_client,
    )
    last_message = chats.get_last_message(chat)
    assert 'Неверно введено имя, пожалуйста введите снова:' == last_message.text

    chat = asserts.assert_text_message_was_handled(
        'Лео',
        chat,
        bot_client,
    )
    last_message = chats.get_last_message(chat)
    assert 'Какой бы была ваша фамилия на букву "Л"?:' == last_message.text

    chat = asserts.assert_text_message_was_handled(
        'Жук',
        chat,
        bot_client,
    )
    last_message = chats.get_last_message(chat)
    assert 'Неверно введена фамилия, пожалуйста введите снова:' == last_message.text

    chat = asserts.assert_text_message_was_handled(
        'Лось',
        chat,
        bot_client,
    )
    last_message = chats.get_last_message(chat)
    assert 'Привет, Лео Лось' == last_message.text

    chat = asserts.assert_command_was_handled(
        '/start',
        chat,
        bot_client,
    )
    last_message = chats.get_last_message(chat)
    assert 'Привет, Я Demo Bot' in  last_message.text
# END test_sequence_example
