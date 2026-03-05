# pylint: disable=duplicate-code
from pathlib import Path
from telegram_framework.test import SimpleTestCase
from telegram_framework.python_telegram_bot import actions
from telegram_framework import chats, messages, keyboards


class MockBot:

    def __init__(self, *args, **kwargs):
        pass

    def send_message(  # pylint: disable=too-many-positional-arguments,too-many-arguments
            self,
            chat_id,
            text,
            parse_mode=None,
            reply_markup=None,
            reply_to_message_id=None,
    ):
        pass

    def send_photo(  # pylint: disable=too-many-positional-arguments,too-many-arguments
            self,
            chat_id,
            photo,
            caption,
            parse_mode,
            reply_markup,
    ):
        pass


class MockUpdater:

    def __init__(self):
        self.bot = MockBot()


class TestActions(SimpleTestCase):

    def setUp(self):
        self.bot = MockUpdater()

    def test_send_message(self):
        """
        Test send_message: success
        """
        chat = chats.Chat()
        self.assertEqual(0, len(chat.messages))
        message = messages.create_message('new message', sender=self.bot)
        keyboard = keyboards.inline.Keyboard(
            buttons=[keyboards.inline.Button('Some button', 'some_data')]
        )
        message = messages.add_keyboard(message, keyboard)
        chat = actions.send_message(chat, message)
        self.assertEqual(1, len(chat.messages))
        last_message = chats.get_last_message(chat)
        self.assertEqual(message, last_message)

    def test_send_image(self):
        """
        Test send_image: success
        """
        chat = chats.Chat()
        self.assertEqual(0, len(chat.messages))
        caption_message = messages.create_message('Image caption', sender=self.bot)
        current_dir = Path(__file__).parent
        image_file_path = current_dir / "data" / "empty.jpg"
        message = messages.create_image(
            sender=self.bot,
            file_path=image_file_path,
            caption=caption_message
        )
        chat = actions.send_image(chat, message)
        self.assertEqual(1, len(chat.messages))
        last_message = chats.get_last_message(chat)
        self.assertIsInstance(last_message, messages.Image)
        self.assertEqual(last_message.caption.text, 'Image caption')
        self.assertEqual(last_message, message)

    def test_send_reply(self):
        """
        Test send_reply: failed: message has no chat
        """
        chat = chats.Chat()
        self.assertEqual(0, len(chat.messages))
        message = messages.create_message('new message', sender=self.bot)
        chat = chats.add_message(chat, message)
        last_message = chats.get_last_message(chat)
        reply = messages.create_reply(last_message, 'reply', sender=self.bot)
        chat = actions.send_reply(reply)
        last_reply = chats.get_last_message(chat)
        expected_reply = messages.create_reply(
            last_message,
            text = 'reply',
            sender=self.bot,
        )
        self.assertEqual(expected_reply, last_reply)

    def test_send_message_force_reply_keyboard(self):
        """
        Test send_message with force.keyboard: success
        """
        chat = chats.Chat()
        self.assertEqual(0, len(chat.messages))
        message = messages.create_message('new message', sender=self.bot)
        keyboard = keyboards.force.Keyboard()
        message = messages.add_keyboard(message, keyboard)
        chat = actions.send_message(chat, message)
        self.assertEqual(1, len(chat.messages))
        last_message = chats.get_last_message(chat)
        self.assertEqual(message, last_message)
        self.assertKeyboardInMessage(last_message)

    def test_send_message_with_reply_keyboard(self):
        """
        Test send_message with reply.keyboard success
        """
        chat = chats.Chat()
        message = messages.create_message('new message', sender=self.bot)
        keyboard = keyboards.reply.Keyboard(
            'Test keyboard',
            buttons=[keyboards.reply.Button('Some button')],
        )
        message = messages.add_keyboard(message, keyboard)
        self.assertKeyboardNotInChat(chat)
        chat = actions.send_message(chat, message)
        self.assertKeyboardInChat(chat)

        message = messages.create_message('new message', sender=self.bot)
        keyboard = keyboards.reply.EmptyKeyboard(
        )
        message = messages.add_keyboard(message, keyboard)
        chat = actions.send_message(chat, message)
        self.assertKeyboardNotInChat(chat)
