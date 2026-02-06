from pyrogram.types import InlineKeyboardMarkup


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
