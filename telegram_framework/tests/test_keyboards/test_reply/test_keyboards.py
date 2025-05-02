from unittest import TestCase
from telegram_framework.keyboards.reply import keyboards, buttons


class TestInline(TestCase):

    def setUp(self):
        self.test_keyboard = keyboards.Keyboard('Test keyboard')

    def test_add_button(self):
        one_button = buttons.Button('One')
        test_keyboard = keyboards.add_button(self.test_keyboard, buttons.Button('One'))
        self.assertEqual(1, len(test_keyboard.buttons))
        self.assertEqual(one_button, test_keyboard.buttons[0])

    def test_add_buttons(self):
        button_list = [
            buttons.Button('One'),
            buttons.Button('Two')
        ]
        test_keyboard = keyboards.add_buttons(self.test_keyboard, button_list)
        self.assertEqual(2, len(test_keyboard.buttons))

    def test_len(self):
        self.assertEqual(0 , len(self.test_keyboard))

    def test_str(self):
        self.assertEqual(self.test_keyboard.name, str(self.test_keyboard))
