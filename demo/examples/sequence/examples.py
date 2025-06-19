from django.core.exceptions import ValidationError
from telegram_framework import keyboards, messages, actions, chats

from .forms import NameForm


# START sequence_example
def start_sequence_example(bot, message):
    keyboard = keyboards.force.Keyboard()
    message_with_text = messages.create_message('Как бы вас звали на букву "Л"?:', sender=bot)
    message_with_keyboard = messages.add_keyboard(message_with_text, keyboard)
    chat = actions.send_message(message.chat, message_with_keyboard)
    chat = actions.wait_response(bot, chat, sequence_first_name_example)
    return chat


def sequence_first_name_example(bot, message):
    first_name = message.text
    if first_name.startswith('Л'):
        chat = chats.add_note(message.chat, first_name=first_name)
        keyboard = keyboards.force.Keyboard()
        message_with_text = messages.create_message(
            'Какой бы была ваша фамилия на букву "Л"?:',
            sender=bot
        )
        message_with_keyboard = messages.add_keyboard(message_with_text, keyboard)
        chat = actions.send_message(chat, message_with_keyboard)
        chat = actions.wait_response(bot, chat, sequence_last_name_example)
        return chat

    keyboard = keyboards.force.Keyboard()
    message_with_text = messages.create_message(
        'Неверно введено имя, пожалуйста введите снова:',
        sender=bot
    )
    message_with_keyboard = messages.add_keyboard(message_with_text, keyboard)
    chat = actions.send_message(message.chat, message_with_keyboard)
    chat = actions.wait_response(bot, chat, sequence_first_name_example)
    return chat


def sequence_last_name_example(bot, message):
    last_name = message.text
    if last_name.startswith('Л'):
        first_name = chats.get_note(message.chat, 'first_name', '?')
        result_text = f'Привет, {first_name} {last_name}'
        message_with_text = messages.create_message(result_text, sender=bot)
        chat = actions.send_message(message.chat, message_with_text)
        return chat

    keyboard = keyboards.force.Keyboard()
    message_with_text = messages.create_message(
        'Неверно введена фамилия, пожалуйста введите снова:',
        sender=bot
    )
    message_with_keyboard = messages.add_keyboard(message_with_text, keyboard)
    chat = actions.send_message(message.chat, message_with_keyboard)
    chat = actions.wait_response(bot, chat, sequence_last_name_example)
    return chat
# END sequence_example


# START sequence_form_example
def name_input(bot, chat, input_text, next_action):
    keyboard = keyboards.force.Keyboard()
    message_with_text = messages.create_message(
        input_text,
        sender=bot
    )
    message_with_keyboard = messages.add_keyboard(message_with_text, keyboard)
    chat = actions.send_message(chat, message_with_keyboard)
    chat = actions.wait_response(bot, chat, next_action)
    return chat

def start_sequence_form_example(bot, message):
    return name_input(
        bot,
        message.chat,
        NameForm.base_fields['first_name'].label,
        sequence_form_first_name_example
    )

def validate_input(bot, message, field_name, action_when_invalid, valid_callback):
    first_name = message.text
    try:
        value = NameForm.base_fields[field_name].clean(first_name)
    except ValidationError as e:
        return name_input(
            bot,
            message.chat,
            e.message,
            action_when_invalid,
        )
    return valid_callback(bot, message, value)

def first_name_valid_callback(bot, message, value):
    chat = chats.add_note(message.chat, first_name=value)
    return name_input(
        bot,
        chat,
        NameForm.base_fields['last_name'].label,
        sequence_form_last_name_example
    )

def sequence_form_first_name_example(bot, message):
    return validate_input(
        bot,
        message,
        'first_name',
        sequence_form_first_name_example,
        first_name_valid_callback,
    )

def last_name_valid_callback(bot, message, value):
    first_name = chats.get_note(message.chat, 'first_name', '?')
    result_text = f'Привет, {first_name} {value}'
    message_with_text = messages.create_message(result_text, sender=bot)
    chat = actions.send_message(message.chat, message_with_text)
    return chat

def sequence_form_last_name_example(bot, message):
    return validate_input(
        bot,
        message,
        'last_name',
        sequence_form_last_name_example,
        last_name_valid_callback,
    )
# END sequence_form_example
