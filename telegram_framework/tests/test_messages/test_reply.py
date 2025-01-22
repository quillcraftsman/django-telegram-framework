from django.test import SimpleTestCase
from telegram_framework.messages.errors import MessageNotInChatError
from telegram_framework.messages.reply import Reply, create_reply
from telegram_framework.messages import Message
from telegram_framework.chat import Chat, add_message, get_last_message

class TestReply(SimpleTestCase):

    def test_create_reply_not_chat(self):
        """
        Test create_reply: failed: message has no chat
        """
        message = Message('new message', sender='some sender')
        with self.assertRaises(MessageNotInChatError):
            create_reply(message, 'should failed', sender='other sender')

    def test_create_reply(self):
        """
        Test create_reply: success
        """
        chat = Chat()
        message = Message('new message', sender='some sender')
        chat = add_message(chat, message)
        last_message = get_last_message(chat)
        reply = create_reply(last_message, 'reply', sender='other sender')
        expected_reply = Reply(
            'reply',
            sender='other sender',
            message=last_message,
            chat=last_message.chat
        )
        self.assertEqual(expected_reply, reply)
