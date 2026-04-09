# pylint: disable=redefined-outer-name
import pytest
from telegram_framework.dummy import bots
from telegram_framework import messages


@pytest.fixture
def bot():
    return bots.get_bot(token='test_dummy')


@pytest.fixture
def some_handler():
    def some_handler_function():
        return 'data'
    return some_handler_function


def test_some_handler_call(some_handler):
    assert 'data' == some_handler()


def test_register_message_handler(some_handler, bot):
    """
    Test register_message_handler: success
    """
    bot = bots.register_message_handler(bot, some_handler)
    assert 1 == len(bot.message_handlers)
    registered_handler = bot.message_handlers[0]
    assert some_handler == registered_handler.function
    assert registered_handler.filter is not None


def test_register_message_handler_filter(some_handler, bot):
    """
    Test register_message_handler with filter: success
    """
    def filter_function(message):  # pylint:disable=unused-argument
        return False

    bot = bots.register_message_handler(bot, some_handler, filter_function)
    assert 1 == len(bot.message_handlers)
    registered_handler = bot.message_handlers[0]
    assert some_handler == registered_handler.function
    assert filter_function == registered_handler.filter  # pylint: disable=comparison-with-callable
    assert not registered_handler.filter(None)


def test_register_text_handler(some_handler, bot):
    """
    Test register_text_handler: success
    """
    bot = bots.register_text_handler(bot, some_handler, 'fixed text')
    assert 1 == len(bot.message_handlers)


def test_register_call_handler(some_handler, bot):
    """
    Test register_call_handler: success
    """
    assert 0 == len(bot.call_handlers)
    bot = bots.register_call_handler(bot, some_handler, 'some_handler')
    assert 1 == len(bot.call_handlers)
    assert some_handler == bot.call_handlers['some_handler'].function


def test_get_bot(bot):
    """
    Test get_bot: success
    """
    bot = bots.get_bot('some_token')
    assert isinstance(bot, bots.DummyBot)


def test_find_handler_command_none(bot):
    """
    Test find_handler: success: no command
    """
    message = messages.Message(text='/some_handler', sender='some_sender')
    handler = bots.find_handler(bot, message)
    assert handler is None


def test_find_handler_message(some_handler, bot):
    """
    Test find_handler: success: message
    """
    bot = bots.register_message_handler(bot, some_handler)
    message = messages.Message(text='some message', sender='some_sender')
    handler = bots.find_handler(bot, message)
    assert some_handler == handler.function


def test_find_handler_message_none(bot):
    """
    Test find_handler: success: no message
    """
    message = messages.Message(text='some message', sender='some_sender')
    handler = bots.find_handler(bot, message)
    assert handler is None


def test_start(bot):
    assert bots.start(bot) is None
