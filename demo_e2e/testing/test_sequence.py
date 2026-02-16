# from pyrogram.types.messages_and_media.message import Message
import pytest
from .functions import (
    wait_response,
    send_message,
)


@pytest.mark.parametrize(
    "command",
    [
        '/sequence_example',
        '/sequence_form_example',
    ]
)
def test_sequence_example(client, command):
    """
    Test sequence_example commands success and validation
    """
    with client:
        # Запускаем последовательность
        send_message(client, command)
        _, text = wait_response(client,1)
        assert 'Как бы вас звали на букву "Л"?:' == text
        # 1-ый раз вводим неправильно
        send_message(client, 'Не на Л')
        _, text = wait_response(client, 1)
        assert 'Неверно введено имя, пожалуйста введите снова:' == text
        # Вводим имя на букву Л
        name = 'Леван'
        send_message(client, name)
        _, text = wait_response(client, 1)
        assert 'Какой бы была ваша фамилия на букву "Л"?:' == text
        # 1-ый раз вводим неправильно
        send_message(client, 'Не на Л')
        _, text = wait_response(client, 1)
        assert 'Неверно введена фамилия, пожалуйста введите снова:' == text
        # Вводим фамилию на букву Л
        surname = 'Ломидзе'
        send_message(client, surname)
        _, text = wait_response(client, 1)
        assert f'Привет, {name} {surname}' == text
