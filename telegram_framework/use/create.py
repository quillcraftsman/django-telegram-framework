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


def create_action(form_cls, result_callback):

    field_keys = list(form_cls.base_fields.keys())
    first_field_key = field_keys[0]
    next_callback = result_callback
    next_action = None

    for key in reversed(field_keys):

        def make_validate_action(key, next_callback):
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

        next_action = make_validate_action(key, next_callback)
        next_action.__name__ = f"validate_{key}_action"
        def make_valid_callback(key, next_action):
            def valid_callback_template(bot, message, value):

                kwargs = {
                    key: value
                }
                chat = chats.add_note(message.chat, **kwargs)

                return field_input(
                    bot,
                    chat,
                    form_cls.base_fields[key].label,
                    next_action,
                )
            return valid_callback_template

        next_callback = make_valid_callback(key, next_action)
        next_callback.__name__=f"valid_{key}_callback"

    def start_sequence(bot, message):
        return field_input(
            bot,
            message.chat,
            form_cls.base_fields[first_field_key].label,
            next_action,
        )

    return start_sequence
