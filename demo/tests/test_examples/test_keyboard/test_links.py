from telegram_framework.test import asserts


# START test_message_with_inline_keyboard_example
def test_message_with_inline_keyboard_example(bot_client, chat):
    """
    Test /message_with_inline_keyboard: success
    """
    chat = asserts.assert_command_was_handled(
        '/message_with_inline_keyboard',
        chat,
        bot_client,
    )
    asserts.assert_chat_last_message_text_equal(
        chat,
        'Пример сообщения с кнопкой',
    )
    keyboard = asserts.assert_chat_last_message_keyboard_len(chat, 1)
    assert 'Нажми меня' == keyboard.buttons[0].text


def test_put_button_handler(bot_client, chat):
    """
    Test button "put_on_me": success
    """
    chat = asserts.assert_call_was_handled(
        'put_on_me',
        chat,
        bot_client,
    )
    asserts.assert_chat_last_message_text_equal(
        chat,
        'Вы нажали кнопку, а я обработал нажатие'
    )
# END test_message_with_inline_keyboard_example


 # START test_message_with_reply_keyboard_example
def test_message_with_reply_keyboard_example(bot_client, chat):
    """
    Test /message_with_reply_keyboard: success
    """
    chat = asserts.assert_command_was_handled(
        '/message_with_reply_keyboard',
        chat,
        bot_client,
    )
    asserts.assert_chat_last_message_text_equal(
        chat,
        'Пример сообщения с клавиатурой',
    )
    asserts.assert_chat_keyboard_len(chat, 1)
    keyboard = asserts.assert_chat_keyboard_name(chat, 'Пример клавиатуры')
    assert 'Нажми меня 🔍' == keyboard.buttons[0].text

def test_put_keyboard_handler(bot_client, chat):
    """
    Test text "Нажми меня 🔍": success
    """
    chat = asserts.assert_text_message_was_handled(
        'Нажми меня 🔍',
        chat,
        bot_client,
    )
    asserts.assert_chat_last_message_text_equal(
        chat,
        'Вы нажали на клавиатуру, а я обработал нажатие и убрал клавиатуру'
    )
    asserts.assert_keyboard_not_in_chat(chat)
# END test_message_with_reply_keyboard_example
