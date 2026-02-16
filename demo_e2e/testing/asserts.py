from pyrogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup


def assert_inline_buttons(message, expected_tuples):
    """
    expected_tuples - (button_text, button_callback_data)
    """
    assert message.reply_markup is not None
    assert isinstance(message.reply_markup, InlineKeyboardMarkup)

    buttons = [
        (button.text, button.callback_data)
        for row in message.reply_markup.inline_keyboard
        for button in row
    ]

    assert len(buttons) == len(expected_tuples)
    assert set(buttons) == set(expected_tuples)


def assert_reply_buttons(message, expected_texts):
    """
    expected_texts - iterable с текстами кнопок
    """

    assert message.reply_markup is not None
    assert isinstance(message.reply_markup, ReplyKeyboardMarkup)

    buttons = [
        button
        for row in message.reply_markup.keyboard
        for button in row
    ]

    assert len(buttons) == len(expected_texts)
    assert set(buttons) == set(expected_texts)
