from telegram_framework import chats
from telegram_framework import messages
from telegram_framework.test import SimpleTestCase


class TestCommands(SimpleTestCase):  # pylint: disable=too-many-public-methods
    ROOT_BOT_LINKS = 'demo.links'

    def test_start(self):
        """
        Test /start: success
        """
        chat = self.assertCommandWasHandled('/start', self.chat)
        last_message = chats.get_last_message(chat)
        expected_text = 'Привет, Я Demo Bot'
        self.assertIn(expected_text, last_message.text)


    def test_help(self):
        """
        Test /help: success
        """
        chat = self.assertCommandWasHandled('/help', self.chat)
        last_message = chats.get_last_message(chat)
        expected_text = 'Привет, Я Demo Bot'
        self.assertIn(expected_text, last_message.text)


    def test_bot_father_commands(self):
        """
        Test /bot_father_commands: success
        """
        chat = self.assertCommandWasHandled('/bot_father_commands', self.chat)
        last_message = chats.get_last_message(chat)
        expected_text = 'commands'
        self.assertIn(expected_text, last_message.text)

    def test_commands(self):
        """
        Test /commands: success
        """
        chat = self.assertCommandWasHandled('/commands', self.chat)
        last_message = chats.get_last_message(chat)
        expected_text = 'commands'
        self.assertIn(expected_text, last_message.text)


    # START test_send_text_message_example
    def test_send_text_message_example(self):
        """
        Test /text_message: success
        """
        chat = self.assertCommandWasHandled('/text_message', self.chat)
        self.assertChatLastMessageTextEqual(
            chat,
            'Пример отправки обычного текстового сообщения',
        )
    # END test_send_text_message_example


    # START test_send_html_message_example
    def test_send_html_message_example(self):
        """
        Test /html_message: success
        """
        chat = self.assertCommandWasHandled('/html_message', self.chat)
        self.assertChatLastMessageTextEqual(
            chat,
            '<b>Пример</b> <i>отправки</i> <s>текстового</s> HTML сообщения',
        )
    # END test_send_html_message_example

    # START test_render_template_example
    def test_render_template_example(self):
        """
        Test /render_template: success
        """
        chat = self.assertCommandWasHandled('/render_template', self.chat)
        self.assertChatLastMessageTextEqual(
            chat,
            '<b>Это</b> <i>сообщение</i> было создано по шаблону',
        )
    # END test_render_template_example

    # START test_echo_answer_example
    def test_echo_answer_example(self):
        """
        Test send any text message: success
        """
        text = 'any message'
        chat = self.assertTextMessageWasHandled(text, self.chat)
        self.assertChatLastMessageTextEqual(
            chat,
             f'На любое неизвестное сообщение я умею присылать его в ответ: {text}',
        )
    # END test_echo_answer_example

    # START test_fixed_text_answer_example
    def test_fixed_text_answer_example(self):
        """
        Test send "Спасибо бот": success
        """
        text = 'Спасибо бот'
        chat = self.assertTextMessageWasHandled(text, self.chat)
        self.assertChatLastMessageTextEqual(
            chat,
             f'На сообщение {text}, я даю фиксированный ответ: Пожалуйста',
        )
    # END test_fixed_text_answer_example

    # START test_contains_text_answer_example
    def test_contains_text_answer_example(self):
        """
        Test send "Спасибо бот": success
        """
        text = 'Привет бот'
        chat = self.assertTextMessageWasHandled(text, self.chat)
        self.assertChatLastMessageTextEqual(
            chat,
             'На сообщение содержащее "Привет", я говорю "И тебе привет"',
        )
    # END test_contains_text_answer_example

    # START test_send_picture_example
    def test_send_picture_example(self):
        """
        Test /send_picture: success
        """
        chat = self.assertCommandWasHandled('/send_picture', self.chat)
        last_message = chats.get_last_message(chat)
        self.assertIsInstance(last_message, messages.Image)
        self.assertIn('logo_1280_640.png', str(last_message.file_path))
    # END test_send_picture_example

    # START test_send_picture_with_caption_example
    def test_send_picture_with_caption_example(self):
        """
        Test /send_picture_with_caption: success
        """
        chat = self.assertCommandWasHandled('/send_picture_with_caption', self.chat)
        last_message = chats.get_last_message(chat)
        self.assertIsNotNone(last_message.caption)
        self.assertEqual('Это логотипы DTF', last_message.caption.text)
    # END test_send_picture_with_caption_example

    # START test_send_picture_with_html_caption_example
    def test_send_picture_with_html_caption_example(self):
        """
        Test /send_picture_with_caption: success
        """
        chat = self.assertCommandWasHandled('/send_picture_with_html_caption', self.chat)
        last_message = chats.get_last_message(chat)
        self.assertIsNotNone(last_message.caption)
        self.assertEqual('Это логотипы <b>DTF</b>', last_message.caption.text)
    # END test_send_picture_with_html_caption_example

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


    # START test_get_user_id_example
    def test_get_user_id_example(self):
        """
        Test /get_user_id
        """
        chat = self.assertCommandWasHandled('/get_user_id', self.chat)
        self.assertChatLastMessageTextEqual(chat, f'Ваш telegram id: {self.client.id}')
    # END test_get_user_id_example


    # START test_send_param_text_message_example
    def test_send_param_text_message_example(self):
        """
        Test /param_text_message <str:param>: success
        """
        chat = self.assertCommandWasHandled('/param_text_message PARAM', self.chat)
        self.assertChatLastMessageTextEqual(
            chat,
            'Пример отправки обычного текстового сообщения с параметром "PARAM"',
        )
    # END test_send_param_text_message_example


    # START test_param_call_buttons_example
    def test_param_call_buttons_example(self):
        """
        Test /param_call_buttons: success
        """
        chat = self.assertCommandWasHandled('/param_call_buttons', self.chat)
        self.assertChatLastMessageTextEqual(
            chat,
            'Кнопки для обработчика с параметром',
        )
        self.assertChatLastMessageKeyboardLen(chat, 2)


    def test_put_button_param_handler(self):
        """
        Test button "put_on_me_params <str:param>": success
        """
        chat = self.assertCallWasHandled('put_on_me_params PARAMPAM', self.chat)
        self.assertChatLastMessageTextEqual(chat, 'Реакция на параметр PARAMPAM')
    # END test_param_call_buttons_example

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
