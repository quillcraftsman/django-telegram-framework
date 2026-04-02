# pylint: disable=redefined-outer-name
from pytest import fixture
from telegram_framework import links, bots, messages


@fixture
def some_handler():
    def some_handler_function(bot):  # pylint: disable=unused-argument
        pass
    return some_handler_function


@fixture
def bot():
    return bots.get_bot('some_token')


def test_mock_handler(some_handler):
    assert some_handler('some_bot') is None


def test_on_message(some_handler, bot):

    on_message_function = links.on_message(some_handler)
    bot = on_message_function(bot)
    message = messages.Message(text='some_text', sender='some_sender')
    handler = bots.find_handler(bot, message)
    assert some_handler == handler.function
    assert 1 == len(bot.message_handlers)


def test_on_text(some_handler, bot):
    on_text_function = links.on_text(some_handler, 'text')
    bot = on_text_function(bot)
    message = messages.Message(text='text', sender='some_sender')
    handler = bots.find_handler(bot, message)
    assert some_handler == handler.function
    assert 1 == len(bot.message_handlers)
