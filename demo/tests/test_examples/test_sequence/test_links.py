from telegram_framework import chats
from telegram_framework.test import SimpleTestCase


class TestCommands(SimpleTestCase):  # pylint: disable=too-many-public-methods
    ROOT_BOT_LINKS = 'demo.links'

    # START test_sequence_example
    def test_sequence_example(self):
        """
        Test /sequence_example
        """
        chat = self.assertCommandWasHandled('/sequence_example', self.chat)
        last_message = self.assertChatLastMessageTextEqual(
            chat,
            'Как бы вас звали на букву "Л"?:',
        )
        self.assertKeyboardInMessage(last_message)

        chat = self.assertTextMessageWasHandled('Жук', chat)
        last_message = chats.get_last_message(chat)
        self.assertEqual('Неверно введено имя, пожалуйста введите снова:', last_message.text)

        chat = self.assertTextMessageWasHandled('Лео', chat)
        last_message = chats.get_last_message(chat)
        self.assertEqual('Какой бы была ваша фамилия на букву "Л"?:', last_message.text)

        chat = self.assertTextMessageWasHandled('Жук', chat)
        last_message = chats.get_last_message(chat)
        self.assertEqual('Неверно введена фамилия, пожалуйста введите снова:', last_message.text)

        chat = self.assertTextMessageWasHandled('Лось', chat)
        last_message = chats.get_last_message(chat)
        self.assertEqual('Привет, Лео Лось', last_message.text)

        chat = self.assertCommandWasHandled('/start', chat)
        last_message = chats.get_last_message(chat)
        self.assertIn('Привет, Я Demo Bot', last_message.text)
    # END test_sequence_example

    # START test_sequence_form_example
    def test_sequence_form_example(self):
        """
        Test /sequence_form_example
        """
        chat = self.assertCommandWasHandled('/sequence_form_example', self.chat)
        last_message = self.assertChatLastMessageTextEqual(
            chat,
            'Как бы вас звали на букву "Л"?:',
        )
        self.assertKeyboardInMessage(last_message)

        chat = self.assertTextMessageWasHandled('Жора', chat)
        last_message = chats.get_last_message(chat)
        self.assertEqual('Неверно введено имя, пожалуйста введите снова:', last_message.text)

        chat = self.assertTextMessageWasHandled('Лора', chat)
        last_message = chats.get_last_message(chat)
        self.assertEqual('Какой бы была ваша фамилия на букву "Л"?:', last_message.text)

        chat = self.assertTextMessageWasHandled('Жора', chat)
        last_message = chats.get_last_message(chat)
        self.assertEqual('Неверно введена фамилия, пожалуйста введите снова:', last_message.text)

        chat = self.assertTextMessageWasHandled('Ларин', chat)
        last_message = chats.get_last_message(chat)
        self.assertEqual('Привет, Лора Ларин', last_message.text)

        chat = self.assertCommandWasHandled('/start', chat)
        last_message = chats.get_last_message(chat)
        self.assertIn('Привет, Я Demo Bot', last_message.text)
    # END test_sequence_form_example
