from .functions import (
    get_last_response
)
from . import asserts


def test_complex_message(client):
    """
    Test /complex_message: success
    """
    command = '/complex_message'
    with client:
        message, text = get_last_response(
            client,
            command,
            answers_count=2,
        )
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
