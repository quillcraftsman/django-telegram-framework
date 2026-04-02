from django.conf import settings
from telegram_framework import (
    chats,
)
from . import asserts


# pylint: disable=invalid-name
class TelegramFrameworkMixin:

    def prepare_bot_and_client(self):
        links_module_name = self.ROOT_BOT_LINKS \
        if hasattr(self, 'ROOT_BOT_LINKS') \
        else settings.ROOT_BOT_LINKS
        self.client, self.chat = asserts.prepare_bot_and_client(links_module_name)

    def _pre_setup(self):
        super()._pre_setup()
        self.prepare_bot_and_client()

    # def assertEmptyChat(self, chat: chats.Chat):
    #     asserts.assert_empty_chat(chat)
    #
    # def assertNotEmptyChat(self, chat: chats.Chat):
    #     asserts.assert_not_empty_chat(chat)

    # def assertChatMessagesCount(self, chat: chats.Chat, count: int, msg=None):
    #     asserts.assert_chat_messages_count(chat, count, msg)

    # def assertChatLastMessageEqual(self, chat: chats.Chat, message):
    #     asserts.assert_chat_last_message_equal(chat, message)

    def assertChatLastMessageTextEqual(self, chat: chats.Chat, text):
        return asserts.assert_chat_last_message_text_equal(
            chat,
            text
        )

    def assertCommandWasHandled(self, command_text, chat, client=None):
        client = client if client else self.client
        return asserts.assert_command_was_handled(command_text, chat, client)

    def assertTextMessageWasHandled(self, text, chat, client=None):
        client = client if client else self.client
        return asserts.assert_text_message_was_handled(text, chat, client)

    # def assertCallWasHandled(self, call_data, chat, client=None):
    #     client = client if client else self.client
    #     return asserts.assert_call_was_handled(call_data, chat, client)

    # def assertKeyboardInChatLastMessage(self, chat):
    #     return asserts.assert_keyboard_in_chat_last_message(chat)

    def assertKeyboardInMessage(self, message):
        return asserts.assert_keyboard_in_message(message)

    def assertKeyboardInChat(self, chat):
        return asserts.assert_keyboard_in_chat(chat)

    def assertKeyboardNotInChat(self, chat):
        asserts.assert_keyboard_not_in_chat(chat)

    # def assertChatLastMessageKeyboardLen(self, chat, value):
    #     return asserts.assert_chat_last_message_keyboard_len(chat, value)
    #
    # def assertChatKeyboardLen(self, chat, value):
    #     return asserts.assert_chat_keyboard_len(chat, value)
    #
    # def assertChatKeyboardName(self, chat, name):
    #     return asserts.assert_chat_keyboard_name(chat, name)
