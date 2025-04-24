from unittest import TestCase
from telegram_framework.keyboards.inline import buttons


class TestInline(TestCase):

    def test_button_defaults(self):
        text = 'Some button'
        data = 'some_data'
        some_button = buttons.Button(
            text=text,
            data=data,
        )
        self.assertEqual(text, some_button.text)
        self.assertEqual(data, some_button.data)
