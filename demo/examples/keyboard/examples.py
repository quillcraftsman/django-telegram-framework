from telegram_framework import keyboards, messages, actions


# START message_with_inline_keyboard_example
def message_with_inline_keyboard_example(bot, message):
    keyboard = keyboards.inline.Keyboard(
        buttons=[
            keyboards.inline.Button('Нажми меня', 'put_on_me'),
        ]
    )
    message_with_text = messages.create_message('Пример сообщения с кнопкой', sender=bot)
    message_with_keyboard = messages.add_keyboard(message_with_text, keyboard)
    return actions.send_message(message.chat, message_with_keyboard)


def put_button_handler(bot, message):
    reply_message = messages.create_message(
        text='Вы нажали кнопку, а я обработал нажатие',
        sender=bot,
    )
    return actions.send_message(message.chat, reply_message)
# END message_with_inline_keyboard_example


# START message_with_reply_keyboard_example
def message_with_reply_keyboard_example(bot, message):
    keyboard = keyboards.reply.Keyboard(
        name = 'Пример клавиатуры',
        buttons=[
            keyboards.reply.Button('Нажми меня 🔍'),
        ]
    )
    message_with_text = messages.create_message('Пример сообщения с клавиатурой', sender=bot)
    message_with_keyboard = messages.add_keyboard(message_with_text, keyboard)
    return actions.send_message(message.chat, message_with_keyboard)


def put_keyboard_handler(bot, message):
    reply_message = messages.create_message(
        text='Вы нажали на клавиатуру, а я обработал нажатие и убрал клавиатуру',
        sender=bot,
    )
    reply_message = messages.add_keyboard(reply_message, keyboards.reply.EmptyKeyboard())
    return actions.send_message(message.chat, reply_message)
# END message_with_reply_keyboard_example
