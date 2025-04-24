from telegram_framework.functions import update


def add_keyboard(message, keyboard):
    return update(message, keyboard=keyboard)
