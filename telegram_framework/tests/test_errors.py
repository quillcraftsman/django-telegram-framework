from telegram_framework import errors


def test_bot_type_error_str():
    error = errors.BotTypeError('SOME_TYPE')
    assert str(error) == 'Unknown BOT_TYPE: SOME_TYPE'
