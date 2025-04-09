from django.test import SimpleTestCase
from telegram_framework.messages.errors import MessageNotInChatError
from telegram_framework.messages.reply import Reply, create_reply
from telegram_framework import messages
from telegram_framework import chats

class TestReply(SimpleTestCase):

    def test_create_reply_not_chat(self):
        """
        Test create_reply: failed: message has no chat
        """
        message = messages.create_message('new message', sender='some sender')
        with self.assertRaises(MessageNotInChatError):
            create_reply(message, 'should failed', sender='other sender')

    def test_create_reply(self):
        """
        Test create_reply: success
        """
        chat = chats.Chat()
        message = messages.create_message('new message', sender='some sender')
        chat = chats.add_message(chat, message)
        last_message = chats.get_last_message(chat)
        reply = create_reply(last_message, 'reply', sender='other sender')
        expected_reply = Reply(
            text='reply',
            sender='other sender',
            message=last_message,
            chat=last_message.chat
        )
        self.assertEqual(expected_reply, reply)
