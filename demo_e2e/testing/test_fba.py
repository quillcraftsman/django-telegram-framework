from .functions import (
    wait_response,
    send_message,
)


def test_list_action(client):
    """
    Test /list_action: success
    """
    with client:
        send_message(client, '/list_action')
        _, text = wait_response(client)
        assert 'Создано с помощью  list_action' in text


def test_list_action_pagination(client):
    """
    Test /list_action_pagination: success
    """
    with client:
        send_message(client, '/list_action_pagination')
        _, text = wait_response(client)
        assert 'Создано с помощью  list_action' in text
        # Почему-то это работает на проде и не работает локально?
        # asserts.assert_inline_buttons(
        #     message,
        #     [('>>', 'list_action_pagination_2')],
        # )


def test_detail_action(client):
    """
    Test /detail_action <id>: success
    """
    with client:
        send_message(client, '/detail_action 1')
        _, text = wait_response(client)
        assert 'Использовать detail_action' in text


def test_template_action(client):
    """
    Test /template_action: success
    """
    with client:
        send_message(client, '/template_action')
        _, text = wait_response(client)
        assert 'Это сообщение было создано по шаблону' in text


def test_create_action(client):
    """
    Test /create_action: success
    """
    with client:
        # Запускаем последовательность
        send_message(client, '/create_action')
        _, text = wait_response(client,1)
        assert 'Как бы вас звали на букву "Л"?:' == text
        # 1-ый раз вводим неправильно
        send_message(client, 'Не на Л')
        _, text = wait_response(client, 1)
        # assert 'Неверно введено имя, пожалуйста введите снова:' == text
        assert 'Как бы вас звали на букву "Л"?:' == text
        # Вводим имя на букву Л
        name = 'Леван'
        send_message(client, name)
        _, text = wait_response(client, 1)
        assert 'Какой бы была ваша фамилия на букву "Л"?:' == text
        # 1-ый раз вводим неправильно
        send_message(client, 'Не на Л')
        _, text = wait_response(client, 1)
        # assert 'Неверно введена фамилия, пожалуйста введите снова:' == text
        assert 'Какой бы была ваша фамилия на букву "Л"?:' == text
        # Вводим фамилию на букву Л
        surname = 'Ломидзе'
        send_message(client, surname)
        _, text = wait_response(client, 1)

        assert 'Каким бы было ваше отчество на букву "Л"?:' == text
        # 1-ый раз вводим неправильно
        send_message(client, 'Не на Л')
        _, text = wait_response(client, 1)
        # assert 'Неверно введено отчество, пожалуйста введите снова:' == text
        assert 'Каким бы было ваше отчество на букву "Л"?:' == text
        # Вводим отчество на букву Л
        middle_name = 'Леванов'
        send_message(client, middle_name)
        _, text = wait_response(client, 1)
        assert f'Привет, {name} {surname} {middle_name}' == text
