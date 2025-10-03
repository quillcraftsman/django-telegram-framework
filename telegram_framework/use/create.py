from django.core.exceptions import ValidationError
from telegram_framework import keyboards, messages, actions, chats


def show_input(form_cls, bot, message, field_name, wait_response_in):
    keyboard = keyboards.force.Keyboard()
    message_with_text = messages.create_message(
        form_cls.base_fields[field_name].label,
        sender=bot
    )
    message_with_keyboard = messages.add_keyboard(message_with_text, keyboard)
    chat = actions.send_message(message.chat, message_with_keyboard)
    chat = actions.wait_response(bot, chat, wait_response_in)
    return chat


def validate_field(form_cls, bot, message, field_name, repeat_function):
    text = message.text
    try:
        value = form_cls.base_fields[field_name].clean(text)
    except ValidationError as e:
        valid = False
        # красные может быть
        # вывод ошибки
        message_with_text = messages.create_message(
            e.message,
            sender=bot
        )
        chat = actions.send_message(message.chat, message_with_text)
        message = chats.get_last_message(chat)
        # return valid, show_input(bot, message, field_name, repeat_function)
        return valid, repeat_function(bot, message)
    valid = True
    # делаем заметку
    chat = message.chat
    kwargs = {
        field_name: value
    }
    chat = chats.add_note(chat, **kwargs)
    form = form_cls(data=chat.notes)
    chat = chats.add_note(chat, form=form)
    return valid, chat


def make_field_functions(form_cls, field_name, next_step_function):

    def validate_field_name(bot, message):
        valid, chat = validate_field(form_cls, bot, message, field_name, enter_field_name)
        if valid:
            message = chats.get_last_message(chat)
            return next_step_function(bot, message)
        return chat

    validate_field_name.__name__ = f'validate_{field_name}_function'

    def enter_field_name(bot, message):
        return show_input(form_cls, bot, message, field_name, validate_field_name)

    enter_field_name.__name__ = f'enter_{field_name}_function'
    return enter_field_name


def create_action(form_cls, result_callback):
    form_field_names = list(form_cls.base_fields.keys())

    next_step_function = result_callback
    enter_field_function = None
    for field_name in reversed(form_field_names):
        enter_field_function = make_field_functions(form_cls, field_name, next_step_function)
        next_step_function = enter_field_function

    return enter_field_function
