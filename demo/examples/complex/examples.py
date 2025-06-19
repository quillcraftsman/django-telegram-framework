from pathlib import Path
from django.conf import settings
from telegram_framework import messages, keyboards, actions


# START complex_message_example
def complex_message_example(bot, message):
    first_message = messages.create_message(
        text='Первая часть сообщения',
        sender=bot,
    )
    keyboard = keyboards.reply.Keyboard(
        name='Пример клавиатуры',
        buttons=[
            keyboards.reply.Button('Нажми меня 🔍'),
        ]
    )
    first_message = messages.add_keyboard(first_message, keyboard)
    chat = actions.send_message(message.chat, first_message)

    file_path = Path(settings.BASE_DIR) / 'static' / 'logo_1280_640.png'
    caption = messages.create_message(
        'Пример <b>комплексного</b> сообщения',
        bot,
        format_type='HTML'
    )
    image = messages.create_image(bot, file_path, caption)

    keyboard = keyboards.inline.Keyboard(
        buttons=[
            keyboards.inline.Button('Нажми меня', 'put_on_me'),
        ]
    )
    image = messages.add_keyboard(image, keyboard)
    return actions.send_image(chat, image)
# END complex_message_example
