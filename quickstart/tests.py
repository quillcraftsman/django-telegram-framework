from telegram_framework import bots, actions, messages, chats, links
from telegram_framework.test import SimpleTestCase
from quickstart.bot import bot_links


class TestCommands(SimpleTestCase):

    def setUp(self):
        # Создайте чат для тестовых сообщений
        chat = chats.Chat()
        # Создайте тестового пользователя
        self.client = bots.get_bot('client')
        # Добавьте его в чат
        chat = chats.add_bot(chat, self.client)
        # Создайте пользователя - бота
        bot = bots.get_bot('bot')
        # Свяжите бота с его обработчиками
        bot = links.add_links(bot, bot_links)
        # Добавьте его в чат
        self.chat = chats.add_bot(chat, bot)
        # В чате пока нет сообщений
        self.assertEqual(0, len(self.chat.messages))

    def test_start(self):
        """
        Test /start: success
        """
        command_text = '/start'
        # Для создания сообщения используйте специальный тип
        # Его будет отправлять клиент sender=self.client
        message = messages.create_message(command_text, sender=self.client)
        # Отправьте его в чат
        chat = actions.send_message(self.chat, message)
        # Бот должен реагировать на сообщения
        # Поэтому в чате будет 2 сообщения
        self.assertChatMessagesCount(chat, 2)
        # Получите последнее сообщение для проверки
        # Оно должно содержать приветствие
        self.assertChatLastMessageTextEqual(chat, 'Приветствую тебя. Я Quickstart Telegram Bot')


    def test_any_text_message(self):
        """
        Test send any text message: success
        """
        # Используйте специальный тип для создания сообщения
        # Его отправит client (sender=self.client)
        message = messages.create_message('quickstart message', sender=self.client)
        # Отправляем сообщение
        chat = actions.send_message(self.chat, message)
        # Бот должен реагировать на сообщение,
        # Поэтому в чате будет 2 сообщения
        self.assertChatMessagesCount(chat, 2)
        # Последнее сообщение должно содержать ответ бота
        self.assertChatLastMessageTextEqual(chat, 'Тебе отвечает Bot')
