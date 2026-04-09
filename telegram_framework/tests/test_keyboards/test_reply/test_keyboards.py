# pylint: disable=redefined-outer-name
import pytest
from telegram_framework.keyboards.reply import keyboards, buttons


@pytest.fixture
def test_keyboard():
    return keyboards.Keyboard('Test keyboard')


def test_add_button(test_keyboard):
    one_button = buttons.Button('One')
    test_keyboard = keyboards.add_button(test_keyboard, buttons.Button('One'))
    assert 1 == len(test_keyboard.buttons)
    assert one_button == test_keyboard.buttons[0]


def test_add_buttons(test_keyboard):
    button_list = [
        buttons.Button('One'),
        buttons.Button('Two')
    ]
    test_keyboard = keyboards.add_buttons(test_keyboard, button_list)
    assert 2== len(test_keyboard.buttons)


def test_len(test_keyboard):
    assert 0 == len(test_keyboard)


def test_str(test_keyboard):
    assert test_keyboard.name == str(test_keyboard)
