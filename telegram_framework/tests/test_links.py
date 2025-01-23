from django.test import SimpleTestCase
from telegram_framework import links, get_bot, find_handler
from telegram_framework.messages import Message

class TestLinks(SimpleTestCase):

    def setUp(self):
        def some_handler(bot):  # pylint: disable=unused-argument
            pass

        self.some_handler = some_handler
        self.bot = get_bot('some_token')

    def test_mock_handler(self):
        self.some_handler('some_bot')

    def test_on_command(self):

        on_command_function = links.on_command(self.some_handler, 'some_command')
        bot = on_command_function(self.bot)
        message = Message(text='/some_command', sender='some_sender')
        handler = find_handler(bot, message)
        self.assertEqual(self.some_handler, handler)
        self.assertEqual(1, len(bot.command_handlers))

    def test_on_message(self):

        on_message_function = links.on_message(self.some_handler)
        bot = on_message_function(self.bot)
        message = Message(text='some_text', sender='some_sender')
        handler = find_handler(bot, message)
        self.assertEqual(self.some_handler, handler)
        self.assertEqual(1, len(bot.message_handlers))

    def test_add_links(self):
        """
        Test add_links: success
        """
        bot_links = [
            links.on_command(self.some_handler, 'one'),
            links.on_command(self.some_handler, 'two')
        ]
        bot = links.add_links(self.bot, bot_links)
        self.assertEqual(2, len(bot.command_handlers))
        for link in bot.command_handlers.values():
            self.assertEqual(self.some_handler, link)
