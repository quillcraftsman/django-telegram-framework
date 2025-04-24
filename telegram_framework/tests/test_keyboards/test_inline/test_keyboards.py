from unittest import TestCase
from telegram_framework.keyboards.inline import keyboards, buttons
from telegram_framework.keyboards.layouts import default_layout

class TestInline(TestCase):

    def setUp(self):
        self.test_keyboard = keyboards.Keyboard()

    def test_keyboard_defaults(self):
        self.assertEqual([], self.test_keyboard.buttons)
        self.assertEqual(default_layout(), self.test_keyboard.layout)

    def test_add_button(self):
        one_button = buttons.Button('One', 'one')
        test_keyboard = keyboards.add_button(self.test_keyboard, buttons.Button('One', 'one'))
        self.assertEqual(1, len(test_keyboard.buttons))
        self.assertEqual(one_button, test_keyboard.buttons[0])

    def test_add_buttons(self):
        button_list = [
            buttons.Button('One', 'one'),
            buttons.Button('Two', 'two')
        ]
        test_keyboard = keyboards.add_buttons(self.test_keyboard, button_list)
        self.assertEqual(2, len(test_keyboard.buttons))

    def test_len(self):
        self.assertEqual(0 , len(self.test_keyboard))
