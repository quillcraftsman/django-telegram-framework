from dataclasses import replace


def add_keyboard(message, keyboard):
    return replace(message, keyboard=keyboard)


# def has_keyboard(message):
#     return message.keyboard is not None
