from telegram_framework import chats
from telegram_framework.test import asserts


# START test_list_action_example
def test_list_action_example(bot_client, chat):
    """
    Test /list_action: success
    """
    chat = asserts.assert_command_was_handled(
        '/list_action',
        chat,
        bot_client,
    )
    assert 'list_action' in chats.get_last_message(chat).text
# END test_list_action_example


# START test_list_action_pagination_example
def test_list_action_pagination_example(bot_client, chat):
    """
    Test /list_action_pagination and call
    list_action_pagination <int:page>: success
    """
    chat = asserts.assert_command_was_handled(
        '/list_action_pagination',
        chat,
        bot_client,
    )
    last_message = chats.get_last_message(chat)
    assert 'Как быстрее писать код для списка' in last_message.text
    asserts.assert_keyboard_in_message(last_message)

    chat = asserts.assert_call_was_handled(
        'list_action_pagination 2',
        chat,
        bot_client,
    )
    last_message = chats.get_last_message(chat)
    assert 'Что это дает' in last_message.text
    asserts.assert_keyboard_in_message(last_message)
# END test_list_action_pagination_example


# START test_detail_action_example
def test_detail_action_example(bot_client, chat):
    """
    Test /detail_action/<int:pk>: success
    """
    # make FAQ
    chat = asserts.assert_command_was_handled(
        '/detail_action 1',
        chat,
        bot_client,
    )
    last_message = chats.get_last_message(chat)
    assert 'detail_action' in last_message.text
    assert 'Использовать detail_action' in last_message.text
# END test_detail_action_example


# START test_template_action_example
def test_template_action_example(bot_client, chat):
    """
    Test /template_action: success
    """
    chat = asserts.assert_command_was_handled(
        '/template_action',
        chat,
        bot_client,
    )
    asserts.assert_chat_last_message_text_equal(
        chat,
        '<b>Это</b> <i>сообщение</i> было создано по шаблону',
    )
# END test_template_action_example


# START test_create_action_example
def test_create_action_example(bot_client, chat):
    """
    Test /create_action
    """
    chat = asserts.assert_command_was_handled(
        '/create_action',
        chat,
        bot_client,
    )
    last_message = asserts.assert_chat_last_message_text_equal(
        chat,
        'Как бы вас звали на букву "Л"?:',
    )
    asserts.assert_keyboard_in_message(last_message)

    chat = asserts.assert_text_message_was_handled(
        'Имя',
        chat,
        bot_client,
    )

    error_message = chat.messages[-2]
    assert 'Неверно введено имя, пожалуйста введите снова:' == error_message.text

    chat = asserts.assert_text_message_was_handled(
        'Лорное Имя',
        chat,
        bot_client,
    )
    last_message = chats.get_last_message(chat)
    assert 'Какой бы была ваша фамилия на букву "Л"?:' == last_message.text

    chat = asserts.assert_text_message_was_handled(
        'Фамилия',
        chat,
        bot_client,
    )
    error_message = chat.messages[-2]
    assert 'Неверно введена фамилия, пожалуйста введите снова:' == error_message.text

    chat = asserts.assert_text_message_was_handled(
        'Лорная Фамилия',
        chat,
        bot_client,
    )
    last_message = chats.get_last_message(chat)
    assert 'Каким бы было ваше отчество на букву "Л"?:' == last_message.text

    chat = asserts.assert_text_message_was_handled(
        'Отчество',
        chat,
        bot_client,
    )
    error_message = chat.messages[-2]
    assert 'Неверно введено отчество, пожалуйста введите снова:' == error_message.text

    chat = asserts.assert_text_message_was_handled(
        'Лорное Отчество',
        chat,
        bot_client,
    )
    last_message = chats.get_last_message(chat)
    assert 'Привет, Лорное Имя Лорная Фамилия Лорное Отчество' == last_message.text

    chat = asserts.assert_command_was_handled(
        '/start',
        chat,
        bot_client,
    )
    last_message = chats.get_last_message(chat)
    assert 'Привет, Я Demo Bot' in last_message.text
# END test_create_action_example
