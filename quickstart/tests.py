from telegram_framework.test import SimpleTestCase


class TestCommands(SimpleTestCase):

    def test_start(self):
        """
        Test /start: success
        """
        # Бот должен реагировать на сообщения
        chat = self.assertCommandWasHandled('/start', self.chat)
        # Последнее сообщение в чате должно содержать приветствие
        self.assertChatLastMessageTextEqual(chat, 'Приветствую тебя. Я Quickstart Telegram Bot')


    def test_any_text_message(self):
        """
        Test send any text message: success
        """
        # Бот должен реагировать на сообщение,
        chat = self.assertTextMessageWasHandled('quickstart message', self.chat)
        # Последнее сообщение должно содержать ответ бота
        self.assertChatLastMessageTextEqual(chat, 'Тебе отвечает Bot')
