from telegram_framework import keyboards, messages, actions, chats


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
