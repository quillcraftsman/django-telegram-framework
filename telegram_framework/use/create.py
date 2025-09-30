from django.core.exceptions import ValidationError
from telegram_framework import keyboards, messages, actions, chats


def field_input(bot, chat, input_text, next_action):
    keyboard = keyboards.force.Keyboard()
    message_with_text = messages.create_message(
        input_text,
        sender=bot
    )
    message_with_keyboard = messages.add_keyboard(message_with_text, keyboard)
    chat = actions.send_message(chat, message_with_keyboard)
    chat = actions.wait_response(bot, chat, next_action)
    return chat


def validate_input(
        bot,
        message,
        form_cls,
        field_name,
        action_when_invalid,
        valid_callback
    ):  # pylint:disable=too-many-arguments,too-many-positional-arguments
    try:
        value = form_cls.base_fields[field_name].clean(message.text)
    except ValidationError as e:
        return field_input(
            bot,
            message.chat,
            e.message,
            action_when_invalid,
        )
    return valid_callback(bot, message, value)


def make_validate_action(key, next_callback, form_cls):
    def validate_action_template(bot, message):
        return validate_input(
            bot,
            message,
            form_cls,
            key,
            validate_action_template,
            next_callback,
        )

    return validate_action_template


def make_valid_callback(current_field_name, previous_field_name, next_action, form_cls):
    def valid_callback_template(bot, message, value):
        kwargs = {
            previous_field_name: value
        }
        chat = chats.add_note(message.chat, **kwargs)
        return field_input(
            bot,
            chat,
            form_cls.base_fields[current_field_name].label,
            next_action,
        )

    return valid_callback_template


def create_action(form_cls, result_callback):

    form_fields = list(form_cls.base_fields.keys())
    first_field = form_fields[0]
    current_callback = result_callback
    current_action = None

    # идем от последнего к 1-му
    # for field_name in reversed(form_fields):
    for i in range(len(form_fields) - 1, -1, -1):

        field_name = form_fields[i]
        previous_field_name = form_fields[i-1]
        current_action = make_validate_action(field_name, current_callback, form_cls)
        current_action.__name__ = f"validate_{field_name}_action"

        # callback становиться этим текущим действием
        current_callback = make_valid_callback(
            field_name,
            previous_field_name,
            current_action,
            form_cls
        )
        current_callback.__name__=f"valid_{field_name}_callback"

    def start_sequence(bot, message):

        return field_input(
            bot,
            message.chat,
            form_cls.base_fields[first_field].label,
            current_action,
        )

    return start_sequence
