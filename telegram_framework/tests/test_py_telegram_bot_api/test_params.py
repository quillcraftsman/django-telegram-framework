from telegram_framework import messages
from telegram_framework.py_telegram_bot_api import params


def test_get_param_command_handler():
    """
    Test function get_param_command_handler: success
    """

    def handler_test(bot, message: messages.Message):  # pylint:disable=unused-argument
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
    assert 'done' == result

    # Вызываем filter_function
    result = filter_function(message)
    assert result

    other_message = messages.create_message(
        '/other_command',
        None,
    )

    result = filter_function(other_message)
    assert not result


def test_get_param_command_handler_with_params():
    """
    Test function get_param_command_handler: success
    Паттерн с параметром
    """

    def handler_test(bot, message: messages.Message, param: str):  # pylint:disable=unused-argument
        return 'done'

    message_text = '/test_command one'

    handler, filter_function = params.get_param_command_handler(
        '/test_command <str:param>',
        handler_test,
    )

    # Вызываем handler

    message = messages.create_message(
        text=message_text,
        sender=None,
    )

    result = handler(None, message)
    assert 'done' == result

    # Вызываем filter_function
    result = filter_function(message)
    assert result

    message = messages.create_message(
        text='/test_command two/error',
        sender=None,
    )

    result = filter_function(message)
    assert not result


def test_get_param_call_handler():
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
    assert 'done' == result

    # Вызываем filter_function
    result = filter_function(call)
    assert result
