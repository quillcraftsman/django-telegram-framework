# pylint: disable=redefined-outer-name
import pytest
from telegram_framework.keyboards.inline import keyboards, buttons
from telegram_framework.keyboards.layouts import default_layout


@pytest.fixture
def test_keyboard():
    return keyboards.Keyboard()


def test_keyboard_defaults(test_keyboard):
    assert [] == test_keyboard.buttons
    assert default_layout() == test_keyboard.layout


def test_add_button(test_keyboard):
    one_button = buttons.Button('One', 'one')
    test_keyboard = keyboards.add_button(test_keyboard, buttons.Button('One', 'one'))
    assert 1 == len(test_keyboard.buttons)
    assert one_button == test_keyboard.buttons[0]


def test_add_buttons(test_keyboard):
    button_list = [
        buttons.Button('One', 'one'),
        buttons.Button('Two', 'two')
    ]
    test_keyboard = keyboards.add_buttons(test_keyboard, button_list)
    assert 2 == len(test_keyboard.buttons)


def test_len(test_keyboard):
    assert 0 == len(test_keyboard)
