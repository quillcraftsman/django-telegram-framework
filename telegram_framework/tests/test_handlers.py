import unittest
from telegram_framework import handlers


class TestHandlers(unittest.TestCase):

    def test_create_handler(self):
        """
        Test create_handler: success
        """
        def handler_function(bot, message):  # pylint:disable=unused-argument
            return True

        description = 'Some text'
        handler = handlers.create_handler(handler_function, description=description)
        self.assertEqual(description, handler.description)
        handler = handlers.create_handler(handler_function)
        self.assertEqual(handler_function.__name__, handler.description)
        self.assertTrue(handler.function(None, None))
