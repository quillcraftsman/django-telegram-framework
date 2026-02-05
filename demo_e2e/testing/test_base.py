from .functions import wait_response,  send_message


def test_start_command(client):
    """
    Test /start: success
    """
    with client:
        send_message(client, '/start')
        _, text = wait_response(client)
        assert 'Я Demo Bot' in text
        assert '/commands' in text


def test_text_message_command(client):
    """
    Test /text_message: success
    """
    with client:
        send_message(client, '/text_message')
        _, text = wait_response(client)
        expected = 'Пример отправки обычного текстового сообщения'
        assert expected == text


def test_html_message_command(client):
    """
    Test /html_message: success
    """
    with client:
        send_message(client, '/html_message')
        _, text = wait_response(client)
        expected = '<b>Пример</b> <i>отправки</i> <s>текстового</s> HTML сообщения'
        assert expected == text.html


def test_render_template_command(client):
    """
    Test /render_template: success
    """
    with client:
        send_message(client, '/render_template')
        _, text = wait_response(client)
        expected = '<b>Это</b> <i>сообщение</i> было создано по шаблону'
        assert expected == text.html


def test_get_user_data_command(client):
    """
    Test /get_user_data: success
    """
    with client:
        send_message(client, '/get_user_data')
        _, text = wait_response(client, timeout=1)
        assert 'Ваш telegram id:' in text
