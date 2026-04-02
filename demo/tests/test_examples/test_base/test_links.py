from telegram_framework import (
    chats,
    messages,
    bots,
)
from telegram_framework.test import asserts
from telegram_framework.user import UserData


# START test_send_text_message_example
def test_send_text_message_example(bot_client, chat):
    """
    Test /text_message: success
    """
    chat = asserts.assert_command_was_handled(
        '/text_message',
        chat,
        bot_client,
    )
    asserts.assert_chat_last_message_text_equal(
        chat,
        'Пример отправки обычного текстового сообщения',
    )
# END test_send_text_message_example


# START test_send_html_message_example
def test_send_html_message_example(bot_client, chat):
    """
    Test /html_message: success
    """
    chat = asserts.assert_command_was_handled(
        '/html_message',
        chat,
        bot_client,
    )
    asserts.assert_chat_last_message_text_equal(
        chat,
        '<b>Пример</b> <i>отправки</i> <s>текстового</s> HTML сообщения',
    )
# END test_send_html_message_example


# START test_render_template_example
def test_render_template_example(bot_client, chat):
    """
    Test /render_template: success
    """
    chat = asserts.assert_command_was_handled(
        '/render_template',
        chat,
        bot_client,
    )
    asserts.assert_chat_last_message_text_equal(
        chat,
        '<b>Это</b> <i>сообщение</i> было создано по шаблону',
    )
# END test_render_template_example


# START test_echo_answer_example
def test_echo_answer_example(bot_client, chat):
    """
    Test send any text message: success
    """
    text = 'any message'
    chat = asserts.assert_text_message_was_handled(
        text,
        chat,
        bot_client,
    )
    asserts.assert_chat_last_message_text_equal(
        chat,
         f'На любое неизвестное сообщение я умею присылать его в ответ: {text}',
    )
# END test_echo_answer_example


 # START test_fixed_text_answer_example
def test_fixed_text_answer_example(bot_client, chat):
    """
    Test send "Спасибо бот": success
    """
    text = 'Спасибо бот'
    chat = asserts.assert_text_message_was_handled(
        text,
        chat,
        bot_client,
    )
    asserts.assert_chat_last_message_text_equal(
        chat,
         f'На сообщение {text}, я даю фиксированный ответ: Пожалуйста',
    )
# END test_fixed_text_answer_example


# START test_contains_text_answer_example
def test_contains_text_answer_example(bot_client, chat):
    """
    Test send "Спасибо бот": success
    """
    text = 'Привет бот'
    chat = asserts.assert_text_message_was_handled(
        text,
        chat,
        bot_client,
    )
    asserts.assert_chat_last_message_text_equal(
        chat,
         'На сообщение содержащее "Привет", я говорю "И тебе привет"',
    )
# END test_contains_text_answer_example


# START test_send_picture_example
def test_send_picture_example(bot_client, chat):
    """
    Test /send_picture: success
    """
    chat = asserts.assert_command_was_handled(
        '/send_picture',
        chat,
        bot_client,
    )
    last_message = chats.get_last_message(chat)
    assert isinstance(last_message, messages.Image)
    assert 'logo_1280_640.png' in str(last_message.file_path)
# END test_send_picture_example


# START test_send_picture_with_caption_example
def test_send_picture_with_caption_example(bot_client, chat):
    """
    Test /send_picture_with_caption: success
    """
    chat = asserts.assert_command_was_handled(
        '/send_picture_with_caption',
        chat,
        bot_client,
    )
    last_message = chats.get_last_message(chat)
    assert last_message.caption is not None
    assert 'Это логотипы DTF' == last_message.caption.text
# END test_send_picture_with_caption_example


# START test_send_picture_with_html_caption_example
def test_send_picture_with_html_caption_example(bot_client, chat):
    """
    Test /send_picture_with_caption: success
    """
    chat = asserts.assert_command_was_handled(
        '/send_picture_with_html_caption',
        chat,
        bot_client,
    )
    last_message = chats.get_last_message(chat)
    assert last_message.caption is not None
    assert 'Это логотипы <b>DTF</b>' == last_message.caption.text
# END test_send_picture_with_html_caption_example


# START test_get_user_data_example
def test_get_user_data_example(chat):
    """
    Test /get_user_data: success
    """
    client_data = UserData(
        123,
        'Client',
        'Test',
        'client',
    )
    client = bots.get_bot(123, client_data)
    chat = asserts.assert_command_was_handled(
        '/get_user_data',
        chat,
        client=client
    )
    asserts.assert_chat_last_message_text_equal(chat, f'Ваш telegram id: {client_data.id}\n'
                                              f'Ваше имя: {client_data.first_name}\n'
                                              f'Ваша фамилия: {client_data.last_name}\n'
                                              f'Ваше имя пользователя {client_data.username}')

def test_get_user_data_not_full(bot_client, chat):
    """
    Test /get_user_data: success not full user data
    """
    chat = asserts.assert_command_was_handled(
        '/get_user_data',
        chat,
        bot_client,
    )
    asserts.assert_chat_last_message_text_equal(
        chat,
        f'Ваш telegram id: {bot_client.user_data.id}\n'
             f'Ваше имя: скрыто\nВаша фамилия: скрыта\n'
             f'Ваше имя пользователя скрыто')
# END test_get_user_data_example


# START test_send_param_text_message_example
def test_send_param_text_message_example(bot_client, chat):
    """
    Test /param_text_message <str:param>: success
    """
    chat = asserts.assert_command_was_handled(
        '/param_text_message PARAM',
        chat,
        bot_client,
    )
    asserts.assert_chat_last_message_text_equal(
        chat,
        'Пример отправки обычного текстового сообщения с параметром "PARAM"',
    )
# END test_send_param_text_message_example


# START test_param_call_buttons_example
def test_param_call_buttons_example(bot_client, chat):
    """
    Test /param_call_buttons: success
    """
    chat = asserts.assert_command_was_handled(
        '/param_call_buttons',
        chat,
        bot_client,
    )
    asserts.assert_chat_last_message_text_equal(
        chat,
        'Кнопки для обработчика с параметром',
    )
    asserts.assert_chat_last_message_keyboard_len(chat, 2)

def test_put_button_param_handler(bot_client, chat):
    """
    Test button "put_on_me_params <str:param>": success
    """
    chat = asserts.assert_call_was_handled(
        'put_on_me_params PARAMPAM',
        chat,
        bot_client,
    )
    asserts.assert_chat_last_message_text_equal(
        chat,
        'Реакция на параметр PARAMPAM',
    )
# END test_param_call_buttons_example


# START test_get_chat_data_example
def test_get_chat_data_example(bot_client, chat):
    """
    Test /chat_data_example: success
    """
    chat = asserts.assert_command_was_handled(
        '/chat_data_example',
        chat,
        bot_client,
    )
    expected_response_text = 'Данные чата: \nid: 0\ntype: dummy\ntitle: None'
    asserts.assert_chat_last_message_text_equal(
        chat,
        expected_response_text,
    )
# END test_get_chat_data_example
