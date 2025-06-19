from telegram_framework.test import SimpleTestCase


class TestCommands(SimpleTestCase):  # pylint: disable=too-many-public-methods
    ROOT_BOT_LINKS = 'demo.links'

    # START test_message_with_inline_keyboard_example
    def test_message_with_inline_keyboard_example(self):
        """
        Test /message_with_inline_keyboard: success
        """
        chat = self.assertCommandWasHandled('/message_with_inline_keyboard', self.chat)
        self.assertChatLastMessageTextEqual(
            chat,
            'Пример сообщения с кнопкой',
        )
        keyboard = self.assertChatLastMessageKeyboardLen(chat, 1)
        self.assertEqual('Нажми меня', keyboard.buttons[0].text)

    def test_put_button_handler(self):
        """
        Test button "put_on_me": success
        """
        chat = self.assertCallWasHandled('put_on_me', self.chat)
        self.assertChatLastMessageTextEqual(chat, 'Вы нажали кнопку, а я обработал нажатие')
    # END test_message_with_inline_keyboard_example

    # START test_message_with_reply_keyboard_example
    def test_message_with_reply_keyboard_example(self):
        """
        Test /message_with_reply_keyboard: success
        """
        chat = self.assertCommandWasHandled('/message_with_reply_keyboard', self.chat)
        self.assertChatLastMessageTextEqual(
            chat,
            'Пример сообщения с клавиатурой',
        )
        self.assertChatKeyboardLen(chat, 1)
        keyboard = self.assertChatKeyboardName(chat, 'Пример клавиатуры')
        self.assertEqual('Нажми меня 🔍', keyboard.buttons[0].text)

    def test_put_keyboard_handler(self):
        """
        Test text "Нажми меня 🔍": success
        """
        chat = self.assertTextMessageWasHandled('Нажми меня 🔍', self.chat)
        self.assertChatLastMessageTextEqual(
            chat,
            'Вы нажали на клавиатуру, а я обработал нажатие и убрал клавиатуру'
        )
        self.assertKeyboardNotInChat(chat)
    # END test_message_with_reply_keyboard_example
