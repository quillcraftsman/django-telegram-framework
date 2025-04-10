from django.test import SimpleTestCase
from telegram_framework import bots
from telegram_framework import actions
from telegram_framework import chats
from telegram_framework.links import add_links
from telegram_framework import messages
from demo.links import bot_links
from demo.models import create_info_text


class TestCommands(SimpleTestCase):

    def setUp(self):
        chat = chats.Chat()
        self.client = bots.get_bot('client')
        chat = chats.add_bot(chat, self.client)
        bot = bots.get_bot('bot')
        bot = add_links(bot, bot_links)
        self.chat = chats.add_bot(chat, bot)
        self.assertEqual(0, len(self.chat.messages))

    def test_start(self):
        """
        Test /start: success
        """
        command_text = '/start'
        message = messages.create_message(command_text, sender=self.client)
        chat = actions.send_message(self.chat, message)
        self.assertEqual(2, len(chat.messages))
        last_message = chats.get_last_message(chat)
        expected_text = create_info_text(command_text)
        self.assertEqual(expected_text, last_message.text)


    def test_help(self):
        """
        Test /help: success
        """
        command_text = '/help'
        message = messages.create_message(command_text, sender=self.client)
        chat = actions.send_message(self.chat, message)
        self.assertEqual(2, len(chat.messages))
        last_message = chats.get_last_message(chat)
        expected_text = create_info_text(command_text)
        self.assertEqual(expected_text, last_message.text)


    # START test_send_text_message_example
    def test_send_text_message_example(self):
        """
        Test /text_message: success
        """
        command_text = '/text_message'
        message = messages.create_message(command_text, sender=self.client)
        chat = actions.send_message(self.chat, message)
        self.assertEqual(2, len(chat.messages))
        last_message = chats.get_last_message(chat)
        expected_text = 'Пример отправки обычного текстового сообщения'
        self.assertEqual(expected_text, last_message.text)
    # END test_send_text_message_example


    # START test_send_html_message_example
    def test_send_html_message_example(self):
        """
        Test /html_message: success
        """
        command_text = '/html_message'
        message = messages.create_message(command_text, sender=self.client)
        chat = actions.send_message(self.chat, message)
        self.assertEqual(2, len(chat.messages))
        last_message = chats.get_last_message(chat)
        expected_text = '<b>Пример</b> <i>отправки</i> <s>текстового</s> HTML сообщения'
        self.assertEqual(expected_text, last_message.text)
    # END test_send_html_message_example

    # START test_render_template_example
    def test_render_template_example(self):
        """
        Test /render_template: success
        """
        command_text = '/render_template'
        message = messages.create_message(command_text, sender=self.client)
        chat = actions.send_message(self.chat, message)
        self.assertEqual(2, len(chat.messages))
        last_message = chats.get_last_message(chat)
        expected_text = '<b>Это</b> <i>сообщение</i> было создано по шаблону'
        self.assertEqual(expected_text, last_message.text)
    # END test_render_template_example


    # START test_echo_answer_example
    def test_echo_answer_example(self):
        """
        Test send any text message: success
        """
        text = 'any message'
        message = messages.create_message('any message', sender=self.client)
        chat = actions.send_message(self.chat, message)
        self.assertEqual(2, len(chat.messages))
        last_message = chats.get_last_message(chat)
        expected_text = f'На любое неизвестное сообщение я умею присылать его в ответ: {text}'
        self.assertEqual(expected_text, last_message.text)
    # END test_echo_answer_example


    # START test_send_picture_example
    def test_send_picture_example(self):
        """
        Test /send_picture: success
        """
        command_text = '/send_picture'
        message = messages.create_message(command_text, sender=self.client)
        chat = actions.send_message(self.chat, message)
        self.assertEqual(2, len(chat.messages))
        last_message = chats.get_last_message(chat)
        self.assertIsInstance(last_message, messages.Image)
        self.assertIn('logo_1280_640.png', str(last_message.file_path))
    # END test_send_picture_example

    # START test_send_picture_with_caption_example
    def test_send_picture_with_caption_example(self):
        """
        Test /send_picture_with_caption: success
        """
        command_text = '/send_picture_with_caption'
        message = messages.create_message(command_text, sender=self.client)
        chat = actions.send_message(self.chat, message)
        self.assertEqual(2, len(chat.messages))
        last_message = chats.get_last_message(chat)
        self.assertIsNotNone(last_message.caption)
        self.assertEqual('Это логотипы DTF', last_message.caption.text)
    # END test_send_picture_with_caption_example

    # START test_send_picture_with_html_caption_example
    def test_send_picture_with_html_caption_example(self):
        """
        Test /send_picture_with_caption: success
        """
        command_text = '/send_picture_with_html_caption'
        message = messages.create_message(command_text, sender=self.client)
        chat = actions.send_message(self.chat, message)
        self.assertEqual(2, len(chat.messages))
        last_message = chats.get_last_message(chat)
        self.assertIsNotNone(last_message.caption)
        self.assertEqual('Это логотипы <b>DTF</b>', last_message.caption.text)
    # END test_send_picture_with_html_caption_example
