from .functions import (
    wait_response,
    send_message,
)
from . import asserts


def test_complex_message(client):
    """
    Test /complex_message: success
    """
    command = '/complex_message'
    with client:
        send_message(client, command)
        message, text = wait_response(client, 1)
        assert text is None
        assert message.photo is not None
        assert message.caption == 'Пример комплексного сообщения'
        # Pyrogram видит только последнюю клавиатуру, прикрепленную
        # к сообщению, это inline, reply из чата он взять не может
        # asserts.assert_reply_buttons(
        #     message,
        #     ['Нажми меня 🔍']
        # )
        asserts.assert_inline_buttons(
            message,
            [('Нажми меня', 'put_on_me')],
        )
