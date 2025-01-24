from django.test import SimpleTestCase
from telegram_framework import get_bot, actions, messages
from telegram_framework.chat import Chat, add_bot, get_last_message
from telegram_framework.links import add_links
from quickstart.bot import bot_links


class TestCommands(SimpleTestCase):

    def setUp(self):
        # Создайте чат для тестовых сообщений
        chat = Chat()
        # Создайте тестового пользователя
        self.client = get_bot('client')
        # Добавьте его в чат
        chat = add_bot(chat, self.client)
        # Создайте пользователя - бота
        bot = get_bot('bot')
        # Свяжите бота с его обработчиками
        bot = add_links(bot, bot_links)
        # Добавьте его в чат
        self.chat = add_bot(chat, bot)
        # В чате пока нет сообщений
        self.assertEqual(0, len(self.chat.messages))

    def test_start(self):
        """
        Test /start: success
        """
        command_text = '/start'
        # Для создания сообщения используйте специальный тип
        # Его будет отправлять клиент sender=self.client
        message = messages.Message(command_text, sender=self.client)
        # Отправьте его в чат
        chat = actions.send_message(self.chat, message)
        # Бот должен реагировать на сообщения
        # Поэтому в чате будет 2 сообщения
        self.assertEqual(2, len(chat.messages))
        # Получите последнее сообщение для проверки
        last_message = get_last_message(chat)
        expected_text = 'Приветствую тебя. Я Quickstart Telegram Bot'
        # Оно должно содержать приветствие
        self.assertEqual(expected_text, last_message.text)


    def test_any_text_message(self):
        """
        Test send any text message: success
        """
        # Используйте специальный тип для создания сообщения
        # Его отправит client (sender=self.client)
        message = messages.Message('quickstart message', sender=self.client)
        # Отправляем сообщение
        chat = actions.send_message(self.chat, message)
        # Бот должен реагировать на сообщение,
        # Поэтому в чате будет 2 сообщения
        self.assertEqual(2, len(chat.messages))
        # Получаем последнее сообщение
        last_message = get_last_message(chat)
        expected_text = 'Тебе отвечает Bot'
        # Оно должно содержать ответ бота
        self.assertEqual(expected_text, last_message.text)
