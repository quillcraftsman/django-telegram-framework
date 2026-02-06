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


def test_any_unknown_message_text(client):
    """
    Test any unknown text message: success
    """
    with client:
        unknown_message = 'Unknown message'
        send_message(client, unknown_message)
        _, text = wait_response(client)
        assert 'На любое неизвестное сообщение я умею присылать его в ответ:' in text
        assert unknown_message


def test_fixed_text_answer(client):
    """
    Test fixed text "Спасибо бот"
    """
    with client:
        fixed_text = 'Спасибо бот'
        send_message(client, fixed_text)
        _, text = wait_response(client)
        assert f'На сообщение {fixed_text}, я даю фиксированный ответ: Пожалуйста' == text


def test_contains_text_answer(client):
    """
    Test when message contains "Привет"
    """
    with client:
        message = 'Это сообщение содержит "Привет"'
        send_message(client, message)
        _, text = wait_response(client)
        assert 'На сообщение содержащее "Привет", я говорю "И тебе привет"' == text


def test_send_param_text_message(client):
    """
    Test command with param "/param_text_message <param>"
    """
    param = 'Test Parameter'
    message = f'/param_text_message {param}'
    with client:
        send_message(client, message)
        _, text = wait_response(client)
        assert f'Пример отправки обычного текстового сообщения с параметром "{param}"' == text
