from telegram_framework.keyboards import inline
from telegram_framework.messages.core import keyboard_message
from telegram_framework import messages


def test_add_keyboard():
    message = messages.create_message('Text', 'sender')
    keyboard = inline.Keyboard()
    message = keyboard_message.add_keyboard(message, keyboard)
    assert keyboard == message.keyboard
