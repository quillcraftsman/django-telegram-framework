# from pyrogram.types.messages_and_media.message import Message
import pytest
from .functions import (
    get_last_response,
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
        _, text = get_last_response(client,command)
        assert 'Как бы вас звали на букву "Л"?:' == text
        # 1-ый раз вводим неправильно
        _, text = get_last_response(client, 'Не на Л')
        assert 'Неверно введено имя, пожалуйста введите снова:' == text
        # Вводим имя на букву Л
        name = 'Леван'
        _, text = get_last_response(client, name)
        assert 'Какой бы была ваша фамилия на букву "Л"?:' == text
        # 1-ый раз вводим неправильно
        _, text = get_last_response(client, 'Не на Л')
        assert 'Неверно введена фамилия, пожалуйста введите снова:' == text
        # Вводим фамилию на букву Л
        surname = 'Ломидзе'
        _, text = get_last_response(client, surname)
        assert f'Привет, {name} {surname}' == text
