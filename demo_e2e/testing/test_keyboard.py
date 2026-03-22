from pyrogram.types import Message
from pyrogram.types.messages_and_media.message import Str
from .functions import (
    get_last_response,
    click_inline_button,
    check_response,
)
from . import asserts


def test_put_on_me_inline_handler(client):
    """
    Test /message_with_inline_keyboard command when put "put_on_me" button
    """
    # Получаем сообщение с кнопкой
    command = '/message_with_inline_keyboard'
    with client:
        message, text = get_last_response(client, command)
        assert 'Пример сообщения с кнопкой' == text
        asserts.assert_inline_buttons(
            message,
            [('Нажми меня', 'put_on_me')],
        )
        callback_data = 'put_on_me'
        # Нажимаем кнопку
        click_inline_button(client, message, callback_data)

        def assert_function(_: Message, text: Str)->None:
            assert 'Вы нажали кнопку, а я обработал нажатие' == text

        check_response(client, assert_function)


def test_put_on_me_reply_handler(client):
    """
    Test /message_with_reply_keyboard command
    when put "put_on_me" reply button
    """
    # Получаем сообщение с кнопкой
    command = '/message_with_reply_keyboard'
    with client:
        message, text = get_last_response(client, command)
        assert 'Пример сообщения с клавиатурой' == text
        reply_button_text = 'Нажми меня 🔍'
        asserts.assert_reply_buttons(
            message,
            [reply_button_text],
        )
        # Отправляем текст в чат
        _, text = get_last_response(client, reply_button_text)
        assert 'Вы нажали на клавиатуру, а я обработал нажатие и убрал клавиатуру' == text
