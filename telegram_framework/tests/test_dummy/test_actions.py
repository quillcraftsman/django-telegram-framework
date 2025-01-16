from django.test import SimpleTestCase
from telegram_framework.dummy.actions import send_message, send_reply
from telegram_framework.chat import Chat, get_last_message, add_message
from telegram_framework.messages import Message, Reply, create_reply


class TestActions(SimpleTestCase):

    def test_send_message(self):
        """
        Test send_message: success
        """
        chat = Chat()
        self.assertEqual(0, len(chat.messages))
        message = Message('new message', sender='some sender')
        chat = send_message(chat, message)
        self.assertEqual(1, len(chat.messages))
        last_message = get_last_message(chat)
        self.assertEqual(message, last_message)

    def test_send_reply(self):
        """
        Test send_reply: failed: message has no chat
        """
        chat = Chat()
        self.assertEqual(0, len(chat.messages))
        message = Message('new message', sender='some sender')
        chat = add_message(chat, message)
        last_message = get_last_message(chat)
        reply = create_reply(last_message, 'reply', sender='other sender')
        chat = send_reply(reply)
        last_reply = get_last_message(chat)
        expected_reply = Reply(
            'reply',
            'other sender',
            message=last_message,
            chat=last_message.chat
        )
        self.assertEqual(expected_reply, last_reply)
