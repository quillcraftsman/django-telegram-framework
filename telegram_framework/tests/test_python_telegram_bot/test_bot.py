from django.test import SimpleTestCase
from telegram.ext.dispatcher import DispatcherHandlerStop
from telegram_framework.python_telegram_bot import bots


class TestPTB(SimpleTestCase):

    def setUp(self):
        self.bot = bots.get_bot('7777777777:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

        def some_handler():
            return 'data'

        self.some_handler = some_handler

    def test_some_handler(self):
        self.assertEqual('data', self.some_handler())
    def test_get_bot(self):
        self.assertIsInstance(self.bot, bots.Updater)

    def test_start(self):
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
        self.assertEqual(1, bot.start_polling_call_count)
        self.assertEqual(1, bot.idle_call_count)

    def test_register_command_handler(self):
        """
        Test register_command_handler: success
        """
        dispatcher = self.bot.dispatcher
        # Там уже есть 1 хэндлер для next_step
        self.assertEqual(1, len(dispatcher.handlers))
        bot = bots.register_command_handler(self.bot, self.some_handler, 'some_handler')
        dispatcher = bot.dispatcher
        self.assertEqual(2, len(dispatcher.handlers))

    def test_register_text_handler(self):
        """
        Test register_text_handler: success
        """
        dispatcher = self.bot.dispatcher
        # Там уже есть 1 хэндлер для next_step
        self.assertEqual(1, len(dispatcher.handlers))
        bot = bots.register_text_handler(self.bot, self.some_handler, 'some_handler')
        dispatcher = bot.dispatcher
        self.assertEqual(2, len(dispatcher.handlers))

    def test_register_call_handler(self):
        """
        Test register_call_handler: success
        """
        dispatcher = self.bot.dispatcher
        # Там уже есть 1 хэндлер для next_step
        self.assertEqual(1, len(dispatcher.handlers))
        bot = bots.register_call_handler(self.bot, self.some_handler, 'some_handler')
        dispatcher = bot.dispatcher
        self.assertEqual(2, len(dispatcher.handlers))

    def test_register_call_handler_with_filter(self):
        """
        Test register_call_handler: success
        with filter_function
        """
        dispatcher = self.bot.dispatcher
        # Там уже есть 1 хэндлер для next_step
        self.assertEqual(1, len(dispatcher.handlers))
        bot = bots.register_call_handler(
            self.bot,
            self.some_handler,
            'some_handler',
            filter_function=lambda _: True,
        )
        dispatcher = bot.dispatcher
        self.assertEqual(2, len(dispatcher.handlers))

    def test_register_message_handler(self):
        """
        Test register_message_handler: success
        """
        dispatcher = self.bot.dispatcher
        # Там уже есть 1 хэндлер для next_step
        self.assertEqual(1, len(dispatcher.handlers))
        bot = bots.register_message_handler(self.bot, self.some_handler, 'some_handler')
        dispatcher = bot.dispatcher
        self.assertEqual(2, len(dispatcher.handlers))

    def test_get_commands_list(self):
        """
        Test get_commands_list: success
        """
        self.assertEqual([], bots.get_commands_list(self.bot))
        handler_name = 'some_handler'
        bot = bots.register_command_handler(self.bot, self.some_handler, handler_name)
        commands_list = bots.get_commands_list(bot)
        self.assertEqual(1, len(commands_list))
        name, _ = commands_list[0]
        self.assertEqual(handler_name, name)

    def test_register_next_step_handler(self):
        """
        Test register_next_step_handler: success
        """
        self.assertEqual(0, len(bots._next_steps))  # pylint: disable=protected-access

        class MockChat:

            def __init__(self):
                self.id = 1

        chat = bots.register_next_step_handler(self.bot, MockChat(), self.some_handler)
        self.assertEqual(1, chat.id)
        self.assertEqual(1, len(bots._next_steps))  # pylint: disable=protected-access

    def test__next_step_router_none(self):
        """
        Test register_next_step_handler: success, return None
        empty next_steps
        """
        bots._next_steps = {}  # pylint: disable=protected-access
        self.assertEqual(0, len(bots._next_steps))  # pylint: disable=protected-access

        class MockChat:

            def __init__(self):
                self.id = 1

        class MockUpdate:

            def __init__(self):
                self.effective_chat = MockChat()

        # pylint: disable=protected-access
        assert bots._next_step_router(MockUpdate(), None) is None

    def test__next_step_router_handler(self):
        """
        Test register_next_step_handler: success, raise DispatcherHandlerStop
        next_steps exists
        """
        bots._next_steps = {}  # pylint: disable=protected-access

        class MockChat:

            def __init__(self):
                self.id = 1

        def mock_handler(_, __):
            return MockChat()

        bots.register_next_step_handler(self.bot, MockChat(), mock_handler)

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
                self.chat = MockChat()

        class MockUpdate:

            def __init__(self):
                self.effective_chat = MockChat()
                self.message = MockMessage()


        with self.assertRaises(DispatcherHandlerStop):
            bots._next_step_router(MockUpdate(), None)  # pylint: disable=protected-access
