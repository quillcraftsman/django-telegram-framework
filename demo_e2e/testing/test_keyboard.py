# from pyrogram.types.messages_and_media.message import Message
from .functions import (
    wait_response,
    send_message,
    click_inline_button,
)
from . import asserts


def test_put_on_me_inline_handler(client):
    """
    Test /message_with_inline_keyboard command when put "put_on_me" button
    """
    # Получаем сообщение с кнопкой
    command = '/message_with_inline_keyboard'
    with client:
        send_message(client, command)
        message, text = wait_response(client, 1)
        assert 'Пример сообщения с кнопкой' == text
        asserts.assert_inline_buttons(
            message,
            [('Нажми меня', 'put_on_me')],
        )
        callback_data = 'put_on_me'
        # Нажимаем кнопку
        click_inline_button(client, message, callback_data)
        _, text = wait_response(client)
        assert 'Вы нажали кнопку, а я обработал нажатие' == text


def test_put_on_me_reply_handler(client):
    """
    Test /message_with_reply_keyboard command
    when put "put_on_me" reply button
    """
    # Получаем сообщение с кнопкой
    command = '/message_with_reply_keyboard'
    with client:
        send_message(client, command)
        message, text = wait_response(client, 1)
        assert 'Пример сообщения с клавиатурой' == text
        reply_button_text = 'Нажми меня 🔍'
        asserts.assert_reply_buttons(
            message,
            [reply_button_text],
        )
        send_message(client, reply_button_text)
        # Отправляем текст в чат
        _, text = wait_response(client, timeout=1)
        assert 'Вы нажали на клавиатуру, а я обработал нажатие и убрал клавиатуру' == text
