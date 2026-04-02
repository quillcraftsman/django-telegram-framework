from telegram_framework import (
    chats,
    keyboards,
    messages,
    actions,
    bots,
    links,
)


def assert_empty_chat(chat: chats.Chat):
    assert chat.messages == [], (
        f"Chat is not empty: {len(chat.messages)} messages\n"
        f"{chat.messages}"
    )


def assert_not_empty_chat(chat: chats.Chat):
    assert bool(chat.messages), (
        "Chat is empty:"
    )


def assert_chat_messages_count(chat: chats.Chat, count: int, msg=None):
    assert len(chat.messages) == count, msg


def assert_chat_last_message_equal(chat: chats.Chat, message):
    last_message = chats.get_last_message(chat)
    assert last_message == message, (
        f"Last message: {last_message}"
        f"not equal to {message}"
    )


def assert_chat_last_message_text_equal(
        chat: chats.Chat,
        text: str
    ):
    last_message =  chats.get_last_message(chat)
    last_message_text = last_message.text
    assert last_message_text == text, (
        f'Last message text: {last_message_text}'
        f'not equal to {text}'
    )
    return last_message


def assert_keyboard_in_message(message):
    keyboard = message.keyboard
    assert message.keyboard is not None, (
        f'Keyboard not in message {message}'
    )
    return keyboard


def assert_keyboard_in_chat(chat):
    keyboard = chat.keyboard
    assert keyboard is not None, (
        f'Keyboard not in chat {chat}'
    )
    return keyboard


def assert_keyboard_not_in_chat(chat):
    keyboard = chat.keyboard
    keyboard_is_none = keyboard is None
    keyboard_is_empty = isinstance(keyboard, keyboards.reply.EmptyKeyboard)
    assert keyboard_is_none or keyboard_is_empty, (
        f'Keyboard "{chat.keyboard}" in chat'
    )


def assert_chat_keyboard_name(chat, name):
    keyboard = assert_keyboard_in_chat(chat)
    assert name == keyboard.name, {
        f'Wrong keyboard name: {keyboard.name},'
        f'expected: {name}'
    }
    return keyboard


def assert_chat_keyboard_len(chat, value):
    keyboard = assert_keyboard_in_chat(chat)
    keyboard_len = len(keyboard)
    assert len(keyboard) == value, (
        f'Keyboard len {keyboard_len} != {value}'
    )
    return keyboard


def assert_keyboard_in_chat_last_message(chat):
    last_message = chats.get_last_message(chat)
    assert_keyboard_in_message(last_message)
    return last_message.keyboard


def assert_text_message_was_handled(text, chat, client):
    message = messages.create_message(text, sender=client)
    chat_messages_count = len(chat.messages)
    chat = actions.send_message(chat, message)
    msg = f'Message "{text}" was not handled'
    assert len(chat.messages) - chat_messages_count > 1, msg
    return chat


def assert_command_was_handled(command_text, chat, client):
    chat = assert_text_message_was_handled(command_text, chat, client)
    return chat


def assert_call_was_handled(call_data, chat, client):
    call = messages.create_call(sender=client, data=call_data)
    chat_messages_count = len(chat.messages)
    chat = actions.send_message(chat, call)
    msg = f'Call "{call_data}" was not handled'
    assert len(chat.messages) - chat_messages_count > 1, msg
    return chat


def prepare_client():
    return bots.get_bot('client')


def prepare_chat(client, links_module_name):
    chat = chats.Chat()
    chat = chats.add_bot(chat, client)
    bot = bots.get_bot('bot')
    bot_links = links.get_root_links(links_module_name)
    bot = links.add_links(bot, bot_links)
    chat = chats.add_bot(chat, bot)
    assert_empty_chat(chat)
    return chat


def prepare_bot_and_client(module_name):
    client = prepare_client()
    chat = prepare_chat(client, module_name)
    return client, chat
