# pylint: disable=redefined-outer-name
import pytest
from telegram_framework.py_telegram_bot_api import bots
from telegram_framework.messages import Message


@pytest.fixture
def bot():
    return bots.get_bot('7777777777:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


@pytest.fixture
def some_handler():
    def some_handler_function():
        return 'data'
    return some_handler_function


def test_some_handler_call(some_handler):
    assert 'data' == some_handler()


def test_register_command_handler(some_handler, bot):
    """
    Test register_command_handler: success
    """
    assert 0 == len(bot.message_handlers)
    bot = bots.register_command_handler(
        bot,
        some_handler,
        'some_handler'
    )
    assert 1 == len(bot.message_handlers)


def test_register_message_handler(some_handler, bot):
    """
    Test register_message_handler
    """
    bot = bots.register_message_handler(bot, some_handler)
    assert 1 == len(bot.message_handlers)


def test_register_text_handler(some_handler, bot):
    """
    Test register_text_handler
    """
    bot = bots.register_text_handler(
        bot,
        some_handler,
        'text'
    )
    assert 1 == len(bot.message_handlers)


def test_register_call_handler(some_handler, bot):
    """
    Test register_call_handler: success
    """
    assert 0 == len(bot.callback_query_handlers)
    bot = bots.register_call_handler(
        bot,
        some_handler,
        'some_handler'
    )
    assert 1 == len(bot.callback_query_handlers)


def test_register_next_step_handler(some_handler, bot):
    """
    Test register_next_step_handler: success
    """
    assert 0 == len(bot.next_step_backend.handlers)

    class MockChat:

        def __init__(self):
            self.id = 1

    chat = bots.register_next_step_handler(
        bot,
        MockChat(),
        some_handler,
    )
    assert 1 == chat.id
    assert 1 == len(bot.next_step_backend.handlers)


def test_get_bot(bot):
    """
    Test get_bot: success
    """
    assert isinstance(bot, bots.TeleBot)


def test_find_handler(bot):
    """
    Test find_handler: success
    """
    message = Message(text='some message', sender='some_sender')
    assert bots.find_handler(bot, message) is None


def test_handle_message(bot):
    """
    Test handle_message success
    """
    class MockMessage:

        def __init__(self):
            self.chat = 'some chat'

    message = MockMessage()
    chat = bots.handle_message(bot, message)
    assert chat == message.chat


def test_start():

    class MockedBot:

        def __init__(self):
            self.infinity_polling_call_count = 0

        def infinity_polling(self):
            self.infinity_polling_call_count += 1

    bot = MockedBot()
    bots.start(bot)
    assert 1 == bot.infinity_polling_call_count


def test_get_commands_list(some_handler, bot):
    """
    Test get_commands_list: success
    """
    assert not bots.get_commands_list(bot)
    handler_name = 'some_handler'
    bot = bots.register_command_handler(
        bot,
        some_handler,
        handler_name
    )
    commands_list = bots.get_commands_list(bot)
    assert 1 == len(commands_list)
    name, _ = commands_list[0]
    assert handler_name == name
