from telegram_framework.keyboards.inline import buttons


def test_button_defaults():
    text = 'Some button'
    data = 'some_data'
    some_button = buttons.Button(
        text=text,
        data=data,
    )
    assert text == some_button.text
    assert data == some_button.data
