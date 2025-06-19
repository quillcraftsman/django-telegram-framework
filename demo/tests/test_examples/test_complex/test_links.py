from telegram_framework import chats
from telegram_framework import messages
from telegram_framework.test import SimpleTestCase


class TestCommands(SimpleTestCase):  # pylint: disable=too-many-public-methods
    ROOT_BOT_LINKS = 'demo.links'

    # START test_complex_message_example
    def test_complex_message_example(self):
        """
        Test /complex_message
        """
        chat = self.assertCommandWasHandled('/complex_message', self.chat)
        self.assertChatMessagesCount(chat, 3)
        last_message = chats.get_last_message(chat)
        self.assertIsInstance(last_message, messages.Image)
        self.assertIn('logo_1280_640.png', str(last_message.file_path))
        self.assertIsNotNone(last_message.caption)
        self.assertEqual('Пример <b>комплексного</b> сообщения', last_message.caption.text)
        self.assertChatKeyboardName(chat, 'Пример клавиатуры')
        keyboard = self.assertChatKeyboardLen(chat, 1)
        self.assertEqual('Нажми меня 🔍', keyboard.buttons[0].text)
        self.assertChatLastMessageKeyboardLen(chat, 1)
    # END test_complex_message_example
