from telegram_framework import (
    chats,
    messages,
)
from telegram_framework.test import asserts


# START test_complex_message_example
def test_complex_message_example(bot_client, chat):
    """
    Test /complex_message
    """
    chat = asserts.assert_command_was_handled(
        '/complex_message',
        chat,
        bot_client,
    )
    asserts.assert_chat_messages_count(chat, 3)
    last_message = chats.get_last_message(chat)
    assert isinstance(last_message, messages.Image)
    assert 'logo_1280_640.png' in str(last_message.file_path)
    assert last_message.caption is not None
    assert 'Пример <b>комплексного</b> сообщения' == last_message.caption.text
    asserts.assert_chat_keyboard_name(chat, 'Пример клавиатуры')
    keyboard = asserts.assert_chat_keyboard_len(chat, 1)
    assert 'Нажми меня 🔍' == keyboard.buttons[0].text
    asserts.assert_chat_last_message_keyboard_len(chat, 1)
# END test_complex_message_example
