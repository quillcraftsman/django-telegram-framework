import unittest
from telegram_framework.keyboards import inline
from telegram_framework.messages.core import keyboard_message
from telegram_framework import messages


class TestKeyboardMessage(unittest.TestCase):

    def test_add_keyboard(self):
        message = messages.create_message('Text', 'sender')
        keyboard = inline.Keyboard()
        message = keyboard_message.add_keyboard(message, keyboard)
        self.assertEqual(keyboard, message.keyboard)
