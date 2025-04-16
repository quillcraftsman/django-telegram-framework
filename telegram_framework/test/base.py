from django.conf import settings
from telegram_framework import (
    chats,
    messages,
    actions,
    bots,
    links,
)


# pylint: disable=invalid-name
class TelegramFrameworkMixin:

    def get_root_bot_links(self):
        module_name = self.ROOT_BOT_LINKS \
            if hasattr(self, 'ROOT_BOT_LINKS') \
            else settings.ROOT_BOT_LINKS
        return links.get_root_links(module_name)

    def prepare_bot_and_client(self):
        chat = chats.Chat()
        self.client = bots.get_bot('client')
        chat = chats.add_bot(chat, self.client)
        bot = bots.get_bot('bot')
        bot_links = self.get_root_bot_links()
        bot = links.add_links(bot, bot_links)
        self.chat = chats.add_bot(chat, bot)
        self.assertEmptyChat(self.chat)

    def _pre_setup(self):
        super()._pre_setup()
        self.prepare_bot_and_client()

    def assertEmptyChat(self, chat: chats.Chat):
        self.assertFalse(chat.messages)

    def assertNotEmptyChat(self, chat: chats.Chat):
        self.assertTrue(chat.messages)

    def assertChatMessagesCount(self, chat: chats.Chat, count: int, msg=None):
        self.assertEqual(len(chat.messages), count, msg)

    def assertChatLastMessageEqual(self, chat: chats.Chat, message):
        self.assertEqual(chats.get_last_message(chat), message)

    def assertChatLastMessageTextEqual(self, chat: chats.Chat, text):
        self.assertEqual(chats.get_last_message(chat).text, text)

    def assertCommandWasHandled(self, command_text, chat, client=None):
        chat = self.assertTextMessageWasHandled(command_text, chat, client)
        return chat

    def assertTextMessageWasHandled(self, text, chat, client=None):
        client = client if client else self.client
        message = messages.create_message(text, sender=client)
        chat = actions.send_message(chat, message)
        msg = f'Message "{text}" was not handled'
        self.assertChatMessagesCount(chat, 2, msg)
        return chat
