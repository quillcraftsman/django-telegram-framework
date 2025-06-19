from telegram_framework import chats
from telegram_framework import messages
from telegram_framework.test import SimpleTestCase


class TestCommands(SimpleTestCase):  # pylint: disable=too-many-public-methods
    ROOT_BOT_LINKS = 'demo.links'

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
