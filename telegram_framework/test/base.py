from django.conf import settings
from telegram_framework import (
    chats,
    messages,
    actions,
    bots,
    links,
    keyboards,
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
        last_message = chats.get_last_message(chat)
        self.assertEqual(last_message.text, text)
        return last_message

    def assertCommandWasHandled(self, command_text, chat, client=None):
        chat = self.assertTextMessageWasHandled(command_text, chat, client)
        return chat

    def assertTextMessageWasHandled(self, text, chat, client=None):
        client = client if client else self.client
        message = messages.create_message(text, sender=client)
        chat_messages_count = len(chat.messages)
        chat = actions.send_message(chat, message)
        msg = f'Message "{text}" was not handled'
        self.assertTrue(len(chat.messages) - chat_messages_count > 1, msg)
        return chat

    def assertCallWasHandled(self, call_data, chat, client=None):
        client = client if client else self.client
        call = messages.create_call(sender=client, data=call_data)
        chat_messages_count = len(chat.messages)
        chat = actions.send_message(chat, call)
        msg = f'Call "{call_data}" was not handled'
        self.assertTrue(len(chat.messages) - chat_messages_count > 1, msg)
        return chat

    def assertKeyboardInChatLastMessage(self, chat):
        last_message = chats.get_last_message(chat)
        self.assertKeyboardInMessage(last_message)
        return last_message.keyboard

    def assertKeyboardInMessage(self, message):
        keyboard = message.keyboard
        self.assertIsNotNone(message.keyboard)
        return keyboard

    def assertKeyboardInChat(self, chat):
        self.assertIsNotNone(chat.keyboard, 'Keyboard not in chat')
        return chat.keyboard

    def assertKeyboardNotInChat(self, chat):
        kayboard = chat.keyboard
        keyboard_is_none = kayboard is None
        keyboard_is_empty = isinstance(kayboard, keyboards.reply.EmptyKeyboard)
        self.assertTrue(
            keyboard_is_none or keyboard_is_empty,
            f'Keyboard "{chat.keyboard}" in chat'
        )

    def assertChatLastMessageKeyboardLen(self, chat, value):
        keyboard = self.assertKeyboardInChatLastMessage(chat)
        self.assertEqual(len(keyboard), value)
        return keyboard

    def assertChatKeyboardLen(self, chat, value):
        keyboard = self.assertKeyboardInChat(chat)
        self.assertEqual(len(keyboard), value)
        return keyboard

    def assertChatKeyboardName(self, chat, name):
        keyboard = self.assertKeyboardInChat(chat)
        self.assertEqual(name, keyboard.name, 'Wrong keyboard name')
        return keyboard
