from telebot import types
from telegram_framework import chats, messages, keyboards, bots


def send_reply(reply: messages.Reply):
    message = reply.message
    text = reply.text
    chat = message.chat
    bot = reply.sender
    bot.reply_to(message, text)
    chat = chats.Chat(id=chat.id)
    return chats.add_message(chat, reply)


def _get_parse_mode(message):
    parse_mode = message.format_type if message.format_type != 'text' else None
    return parse_mode


def send_image(chat: chats.Chat, image: messages.Image):
    bot = image.sender
    parse_mode = None
    caption_text = None
    if image.caption:
        parse_mode = _get_parse_mode(image.caption)
        caption_text = image.caption.text
    reply_markup = _make_reply_markup(image)
    with open(image.file_path, "rb") as f:
        bot.send_photo(
            chat_id=chat.id,
            photo=f,
            caption=caption_text,
            parse_mode=parse_mode,
            reply_markup=reply_markup,
        )
    chat = chats.Chat(id=chat.id)
    return chats.add_message(chat, image)


def _make_reply_markup(message):
    markup = None
    keyboard = message.keyboard
    if not keyboard:
        markup = None
    elif isinstance(keyboard, keyboards.inline.Keyboard):
        markup = types.InlineKeyboardMarkup(row_width=keyboard.layout.columns_count)
        button_list = [
            types.InlineKeyboardButton(button.text, callback_data=button.data)
            for button in keyboard.buttons
        ]
        # Надо передавать кнопки все сразу, иначе не работает row_width в разметке
        markup.add(*button_list)
    elif isinstance(keyboard, keyboards.reply.Keyboard):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for button in keyboard.buttons:
            markup.row(
                types.KeyboardButton(button.text),
            )
    elif isinstance(keyboard, keyboards.force.Keyboard):
        markup = types.ForceReply(selective=keyboard.selective)
    elif isinstance(keyboard, keyboards.reply.EmptyKeyboard):
        markup = types.ReplyKeyboardRemove()
    return markup

def _send_message(chat: chats.Chat, message: messages.Message, parse_mode=None):
    bot = message.sender
    text = message.text
    reply_markup = _make_reply_markup(message)
    bot.send_message(
        chat.id,
        text,
        parse_mode=parse_mode,
        reply_markup=reply_markup,
    )
    # chat = chats.Chat(id=chat.id)
    return chats.add_message(chat, message)


def send_message(chat: chats.Chat, message: messages.Message):
    parse_mode = _get_parse_mode(message)
    return _send_message(chat, message, parse_mode)


def wait_response(bot, chat, handler):  # pragma: no cover
    chat = bots.register_next_step_handler(bot, chat, handler)
    return chat
