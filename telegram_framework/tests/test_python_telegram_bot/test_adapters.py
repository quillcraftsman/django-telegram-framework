# pylint: disable=redefined-outer-name
import pytest
from telegram_framework import chats
from telegram_framework.python_telegram_bot import adapters, bots


@pytest.fixture
def bot():
    return bots.get_bot('7777777777:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


def test_prepare_handler(bot):

    current_chat = chats.Chat(id=0)

    def handler_function(current_bot, message):  # pylint: disable=unused-argument
        return current_chat

    prepared_function = adapters.prepare_handler(handler_function, bot)

    class MockUser:

        def __init__(self):
            self.id = '123456'
            self.first_name = 'Mock'
            self.last_name = 'Mock'
            self.username = 'Mock'

    class MockChat:

        def __init__(self):
            self.id = 0

    class MockMessage:

        def __init__(self):
            self.from_user = MockUser()
            self.text = 'mock text'
            self.reply_markup = None
            self.message_id = 0
            self.chat = MockChat()

    class MockUpdate:

        def __init__(self):
            self.message = MockMessage()

    assert prepared_function(MockUpdate(), None) == current_chat


def test_prepare_call_handler(bot):

    current_chat = chats.Chat(id=0)

    def handler_function(current_bot, context):  # pylint: disable=unused-argument
        return current_chat

    prepared_function = adapters.prepare_call_handler(
        handler_function,
        bot,
    )

    class MockUser:

        def __init__(self):
            self.id = 'test user'
            self.first_name = 'test name'
            self.last_name = 'test name'
            self.username = 'testname'

    class MockChat:

        def __init__(self):
            self.id = '0'

    class MockMessage:

        def __init__(self):
            self.chat = MockChat()

    class MockCallbackQuery:

        def __init__(self):
            self.from_user = MockUser()
            self.data = 'call data'
            self.message = MockMessage()

    class MockUpdate:

        def __init__(self):
            self.message = None
            self.callback_query = MockCallbackQuery()

    update = MockUpdate()
    result = prepared_function(update, None)
    assert current_chat == result
