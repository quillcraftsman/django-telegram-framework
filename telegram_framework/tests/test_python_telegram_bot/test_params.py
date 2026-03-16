from django.test import SimpleTestCase
from telegram_framework import messages
from telegram_framework.python_telegram_bot import params


class TestParams(SimpleTestCase):

    def test_get_param_command_handler(self):
        """
        Test function get_param_command_handler: success
        """
        def handler_test(bot, message: messages.Message): # pylint:disable=unused-argument
            return 'done'

        message_text = '/test_command'

        handler, filter_function = params.get_param_command_handler(
            message_text,
            handler_test,
        )

        # Вызываем handler

        message = messages.create_message(
            text=message_text,
            sender=None,
        )

        result = handler(None, message)
        self.assertEqual('done', result)

        # Вызываем filter_function
        result = filter_function(message_text)
        self.assertTrue(result)
        result = filter_function('/other_command')
        self.assertFalse(result)

    def test_get_param_call_handler(self):
        """
        Test function get_param_call_handler: success
        """
        def handler_test(bot, message: messages.Call): # pylint:disable=unused-argument
            return 'done'

        call_data = 'test_data'

        handler, filter_function = params.get_param_call_handler(
            call_data,
            handler_test,
        )

        # Вызываем handler
        call = messages.create_call(
            None,
            call_data,
        )
        result = handler(None, call)
        self.assertEqual('done', result)

        # Вызываем filter_function
        result = filter_function(call_data)
        self.assertTrue(result)
