from django.test import SimpleTestCase
from telegram_framework.dummy.actions import send_message, send_reply
from telegram_framework import chats, messages


class TestActions(SimpleTestCase):

    def test_send_message(self):
        """
        Test send_message: success
        """
        chat = chats.Chat()
        self.assertEqual(0, len(chat.messages))
        message = messages.create_message('new message', sender='some sender')
        chat = send_message(chat, message)
        self.assertEqual(1, len(chat.messages))
        last_message = chats.get_last_message(chat)
        self.assertEqual(message, last_message)

    def test_send_reply(self):
        """
        Test send_reply: failed: message has no chat
        """
        chat = chats.Chat()
        self.assertEqual(0, len(chat.messages))
        message = messages.create_message('new message', sender='some sender')
        chat = chats.add_message(chat, message)
        last_message = chats.get_last_message(chat)
        reply = messages.create_reply(last_message, 'reply', sender='other sender')
        chat = send_reply(reply)
        last_reply = chats.get_last_message(chat)
        # expected_reply = messages.Reply(
        #     'reply',
        #     'other sender',
        #     message=last_message,
        #     chat=last_message.chat
        # )
        self.assertEqual(reply, last_reply)

    # def test_wait_response(self):
    #     """
    #     Test wait_response: success
    #     """
    #     bot = bots.get_bot(0)
    #     chat = chats.Chat()
    #
    #     def handler(bot, message):
    #         return chat
    #
    #     new_chat = wait_response(
    #         bot,
    #         chat,
    #         handler
    #     )
    #     self.assertEqual(new_chat, chat)
