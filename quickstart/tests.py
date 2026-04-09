# pylint: disable=redefined-outer-name
from pytest import fixture
from telegram_framework.test import asserts


@fixture
def bot_client():
    client = asserts.prepare_client()
    return client


@fixture
def chat(bot_client):  # pylint: disable=redefined-outer-name
    return asserts.prepare_chat(bot_client, 'quickstart.bot')


def test_start(bot_client, chat):
    """
    Test /start: success
    """
    # Бот должен реагировать на сообщения
    chat = asserts.assert_command_was_handled(
        '/start',
        chat,
        bot_client,
    )
    # Последнее сообщение в чате должно содержать приветствие
    asserts.assert_chat_last_message_text_equal(
        chat,
        'Приветствую тебя. Я Quickstart Telegram Bot'
    )


def test_any_text_message(bot_client, chat):
    """
    Test send any text message: success
    """
    # Бот должен реагировать на сообщение,
    chat = asserts.assert_text_message_was_handled(
        'quickstart message',
        chat,
        bot_client,
    )
    # Последнее сообщение должно содержать ответ бота
    asserts.assert_chat_last_message_text_equal(
        chat,
        'Тебе отвечает Bot'
    )
