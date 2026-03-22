from .functions import (
    get_last_response,
)
from . import asserts


def test_list_action(client):
    """
    Test /list_action: success
    """
    with client:
        _, text = get_last_response(client, '/list_action')
        assert 'Создано с помощью  list_action' in text


def test_list_action_pagination(client):
    """
    Test /list_action_pagination: success
    """
    with client:
        message, text = get_last_response(client, '/list_action_pagination')
        assert 'Создано с помощью  list_action' in text
        # Почему-то это работает на проде и не работает локально?
        asserts.assert_inline_buttons(
            message,
            [('>>', 'list_action_pagination 2')],
        )


def test_detail_action(client):
    """
    Test /detail_action <id>: success
    """
    with client:
        _, text = get_last_response(client, '/detail_action 1')
        assert 'Использовать detail_action' in text


def test_template_action(client):
    """
    Test /template_action: success
    """
    with client:
        _, text = get_last_response(client, '/template_action')
        assert 'Это сообщение было создано по шаблону' in text


def test_create_action(client):
    """
    Test /create_action: success
    """
    with client:
        # Запускаем последовательность
        _, text = get_last_response(client,'/create_action')
        assert 'Как бы вас звали на букву "Л"?:' == text
        # 1-ый раз вводим неправильно
        _, text = get_last_response(client, 'Не на Л', answers_count=2)
        # assert 'Неверно введено имя, пожалуйста введите снова:' == text
        assert 'Как бы вас звали на букву "Л"?:' == text
        # Вводим имя на букву Л
        name = 'Леван'
        _, text = get_last_response(client, name)
        assert 'Какой бы была ваша фамилия на букву "Л"?:' == text
        # 1-ый раз вводим неправильно
        _, text = get_last_response(client, 'Не на Л', answers_count=2)
        # assert 'Неверно введена фамилия, пожалуйста введите снова:' == text
        assert 'Какой бы была ваша фамилия на букву "Л"?:' == text
        # Вводим фамилию на букву Л
        surname = 'Ломидзе'
        _, text = get_last_response(client, surname)

        assert 'Каким бы было ваше отчество на букву "Л"?:' == text
        # 1-ый раз вводим неправильно
        _, text = get_last_response(client, 'Не на Л', answers_count=2)
        # assert 'Неверно введено отчество, пожалуйста введите снова:' == text
        assert 'Каким бы было ваше отчество на букву "Л"?:' == text
        # Вводим отчество на букву Л
        middle_name = 'Леванов'
        _, text = get_last_response(client, middle_name)
        assert f'Привет, {name} {surname} {middle_name}' == text
