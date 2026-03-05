import telegram
from telegram.ext.updater import Updater
from telegram_framework import chats, messages, keyboards


def send_image(chat: chats.Chat, image: messages.Image):
    bot: Updater = image.sender
    parse_mode = None
    caption_text = None
    if image.caption:
        parse_mode = _get_parse_mode(image.caption)
        caption_text = image.caption.text
    reply_markup = _make_reply_markup(image)
    with open(image.file_path, "rb") as f:
        bot.bot.send_photo(
            chat_id=chat.id,
            photo=f,
            caption=caption_text,
            parse_mode=parse_mode,
            reply_markup=reply_markup,
        )
    chat = chats.Chat(id=chat.id)
    return chats.add_message(chat, image)



def send_reply(reply: messages.Reply):
    message = reply.message
    text = reply.text
    chat = message.chat
    bot: Updater = reply.sender
    bot.bot.send_message(
        chat_id=chat.id,
        text=text,
        reply_to_message_id=getattr(message, 'id', None),  # id сообщения для ответа
    )
    chat = chats.Chat(id=chat.id)
    return chats.add_message(chat, reply)


def _make_reply_markup(message):
    markup = None
    keyboard = message.keyboard

    if not keyboard:
        markup = None

    elif isinstance(keyboard, keyboards.inline.Keyboard):
        # Inline кнопки
        button_list = [
            telegram.InlineKeyboardButton(text=button.text, callback_data=button.data)
            for button in keyboard.buttons
        ]
        # PTB также принимает *button_list для add, row_width задаём через InlineKeyboardMarkup
        markup = telegram.InlineKeyboardMarkup(
            inline_keyboard=[
                button_list[i:i + keyboard.layout.columns_count]
                for i in range(0, len(button_list), keyboard.layout.columns_count)
            ]
        )

    elif isinstance(keyboard, keyboards.reply.Keyboard):
        # Reply клавиатура
        rows = []
        for button in keyboard.buttons:
            rows.append([telegram.KeyboardButton(text=button.text)])
        markup = telegram.ReplyKeyboardMarkup(
            keyboard=rows,
            resize_keyboard=True
        )
    elif isinstance(keyboard, keyboards.force.Keyboard):
        # ForceReply
        markup = telegram.ForceReply(selective=keyboard.selective)

    elif isinstance(keyboard, keyboards.reply.EmptyKeyboard):
        # Удаление клавиатуры
        markup = telegram.ReplyKeyboardRemove()

    return markup


def _send_message(chat: chats.Chat, message: messages.Message, parse_mode=None):
    bot: Updater = message.sender
    text = message.text
    reply_markup = _make_reply_markup(message)
    bot.bot.send_message(
        chat.id,
        text,
        parse_mode=parse_mode,
        reply_markup=reply_markup,
    )
    return chats.add_message(chat, message)

# Дублируется в Telebot, зависит от message надо перенести в core пакет
def _get_parse_mode(message):
    parse_mode = message.format_type if message.format_type != 'text' else None
    return parse_mode

def send_message(chat: chats.Chat, message: messages.Message):
    parse_mode = _get_parse_mode(message)
    return _send_message(chat, message, parse_mode)
