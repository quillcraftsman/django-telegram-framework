from telegram_framework import chats
from telegram_framework.test import SimpleTestCase


class TestCommands(SimpleTestCase):  # pylint: disable=too-many-public-methods
    ROOT_BOT_LINKS = 'demo.links'

    # START test_list_action_example
    def test_list_action_example(self):
        """
        Test /list_action: success
        """
        chat = self.assertCommandWasHandled('/list_action', self.chat)
        self.assertIn('list_action', chats.get_last_message(chat).text)
    # END test_list_action_example

    # START test_list_action_pagination_example
    def test_list_action_pagination_example(self):
        """
        Test /list_action_pagination and call list_action_pagination <int:page>: success
        """
        chat = self.assertCommandWasHandled('/list_action_pagination', self.chat)
        last_message = chats.get_last_message(chat)
        self.assertIn('Как быстрее писать код для списка', last_message.text)
        self.assertKeyboardInMessage(last_message)

        chat = self.assertCallWasHandled('list_action_pagination 2', self.chat)
        last_message = chats.get_last_message(chat)
        self.assertIn('Что это дает', last_message.text)
        self.assertKeyboardInMessage(last_message)
    # END test_list_action_pagination_example

    # START test_detail_action_example
    def test_detail_action_example(self):
        """
        Test /detail_action/<int:pk>: success
        """
        # make FAQ
        chat = self.assertCommandWasHandled('/detail_action 1', self.chat)
        last_message = chats.get_last_message(chat)
        self.assertIn('detail_action', last_message.text)
        self.assertIn('Использовать detail_action', last_message.text)
    # END test_detail_action_example

    # START test_template_action_example
    def test_template_action_example(self):
        """
        Test /template_action: success
        """
        chat = self.assertCommandWasHandled('/template_action', self.chat)
        self.assertChatLastMessageTextEqual(
            chat,
            '<b>Это</b> <i>сообщение</i> было создано по шаблону',
        )
    # END test_template_action_example

    # START test_create_action_example
    def test_create_action_example(self):
        """
        Test /create_action
        """
        chat = self.assertCommandWasHandled('/create_action', self.chat)
        last_message = self.assertChatLastMessageTextEqual(
            chat,
            'Как бы вас звали на букву "Л"?:',
        )
        self.assertKeyboardInMessage(last_message)

        chat = self.assertTextMessageWasHandled('Имя', chat)

        error_message = chat.messages[-2]
        self.assertEqual('Неверно введено имя, пожалуйста введите снова:', error_message.text)

        chat = self.assertTextMessageWasHandled('Лорное Имя', chat)
        last_message = chats.get_last_message(chat)
        self.assertEqual('Какой бы была ваша фамилия на букву "Л"?:', last_message.text)

        chat = self.assertTextMessageWasHandled('Фамилия', chat)
        error_message = chat.messages[-2]
        self.assertEqual('Неверно введена фамилия, пожалуйста введите снова:', error_message.text)

        chat = self.assertTextMessageWasHandled('Лорная Фамилия', chat)
        last_message = chats.get_last_message(chat)
        self.assertEqual('Каким бы было ваше отчество на букву "Л"?:', last_message.text)

        chat = self.assertTextMessageWasHandled('Отчество', chat)
        error_message = chat.messages[-2]
        self.assertEqual('Неверно введено отчество, пожалуйста введите снова:', error_message.text)

        chat = self.assertTextMessageWasHandled('Лорное Отчество', chat)
        last_message = chats.get_last_message(chat)
        self.assertEqual('Привет, Лорное Имя Лорная Фамилия Лорное Отчество', last_message.text)

        chat = self.assertCommandWasHandled('/start', chat)
        last_message = chats.get_last_message(chat)
        self.assertIn('Привет, Я Demo Bot', last_message.text)
    # END test_create_action_example
