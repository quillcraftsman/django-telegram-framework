# pylint: disable=redefined-outer-name
import pytest
from telegram.ext.dispatcher import DispatcherHandlerStop
from telegram_framework import chats
from telegram_framework.python_telegram_bot import bots



@pytest.fixture
def bot():
    return bots.get_bot('7777777777:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


@pytest.fixture
def some_handler():
    def some_handler_function():
        return 'data'

    return some_handler_function


def test_some_handler(some_handler):
    assert 'data' == some_handler()


def test_get_bot(bot):
    assert isinstance(bot, bots.Updater)


def test_start():

    class MockedBot:

        def __init__(self):
            self.start_polling_call_count = 0
            self.idle_call_count = 0

        def start_polling(self):
            self.start_polling_call_count += 1

        def idle(self):
            self.idle_call_count += 1

    bot = MockedBot()
    bots.start(bot)
    assert 1 == bot.start_polling_call_count
    assert 1 == bot.idle_call_count


def test_register_command_handler(bot, some_handler):
    """
    Test register_command_handler: success
    """
    dispatcher = bot.dispatcher
    # Там уже есть 1 хэндлер для next_step
    current_handlers_count = len(dispatcher.handlers)
    bot = bots.register_command_handler(
        bot,
        some_handler,
        'some_handler'
    )
    dispatcher = bot.dispatcher
    assert current_handlers_count + 1 == len(dispatcher.handlers)


def test_register_text_handler(bot, some_handler):
    """
    Test register_text_handler: success
    """
    dispatcher = bot.dispatcher
    # Там уже есть 1 хэндлер для next_step
    current_handlers_count = len(dispatcher.handlers)
    bot = bots.register_text_handler(
        bot,
        some_handler,
        'some_handler'
    )
    dispatcher = bot.dispatcher
    assert current_handlers_count + 1 == len(dispatcher.handlers)


def test_register_call_handler(bot, some_handler):
    """
    Test register_call_handler: success
    """
    dispatcher = bot.dispatcher
    # Там уже есть 1 хэндлер для next_step
    current_handlers_count = len(dispatcher.handlers)
    bot = bots.register_call_handler(
        bot,
        some_handler,
        'some_handler'
    )
    dispatcher = bot.dispatcher
    assert current_handlers_count + 1 == len(dispatcher.handlers)


def test_register_call_handler_with_filter(bot):
    """
    Test register_call_handler: success
    with filter_function
    """
    dispatcher = bot.dispatcher
    # Там уже есть 1 хэндлер для next_step
    current_handlers_count = len(dispatcher.handlers)

    bot = bots.register_call_handler(
        bot,
        some_handler,
        'some_handler',
        filter_function=lambda _: True,
    )
    dispatcher = bot.dispatcher
    assert current_handlers_count + 1 == len(dispatcher.handlers)


def test_register_message_handler(bot):
    """
    Test register_message_handler: success
    """
    dispatcher = bot.dispatcher
    # Там уже есть 1 хэндлер для next_step
    current_handlers_count = len(dispatcher.handlers)
    bot = bots.register_message_handler(
        bot,
        some_handler,
        'some_handler'
    )
    dispatcher = bot.dispatcher
    assert current_handlers_count + 1 == len(dispatcher.handlers)


def test_get_commands_list(bot, some_handler):
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


def test_register_next_step_handler(bot, some_handler):
    """
    Test register_next_step_handler: success
    """
    assert 0 == len(bots._next_steps)  # pylint: disable=protected-access

    class MockChat:

        def __init__(self):
            self.id = 1

    chat = bots.register_next_step_handler(
        bot,
        MockChat(),
        some_handler
    )
    assert 1 == chat.id
    assert 1 == len(bots._next_steps)  # pylint: disable=protected-access


def test__next_step_router_none():
    """
    Test register_next_step_handler: success, return None
    empty next_steps
    """
    bots._next_steps = {}  # pylint: disable=protected-access
    assert 0 == len(bots._next_steps)  # pylint: disable=protected-access

    class MockChat:

        def __init__(self):
            self.id = 1

    class MockUpdate:

        def __init__(self):
            self.effective_chat = MockChat()

    # pylint: disable=protected-access
    assert bots._next_step_router(MockUpdate(), None) is None


def test__next_step_router_handler(bot):
    """
    Test register_next_step_handler: success, raise DispatcherHandlerStop
    next_steps exists
    """
    bots._next_steps = {}  # pylint: disable=protected-access

    chat = chats.Chat()

    def mock_handler(_, __):
        return chat

    bots.register_next_step_handler(bot, chat, mock_handler)

    class MockUser:

        def __init__(self):
            self.id = 1
            self.first_name = 'mock'
            self.last_name = 'mock'
            self.username = 'mock'

    class MockMessage:

        def __init__(self):
            self.message_id = 1
            self.text = 'some text'
            self.from_user = MockUser()
            self.reply_markup = 'html'
            self.chat = chat

    class MockUpdate:

        def __init__(self):
            self.effective_chat = chat
            self.message = MockMessage()

    with pytest.raises(DispatcherHandlerStop):
        bots._next_step_router(MockUpdate(), None)  # pylint: disable=protected-access
