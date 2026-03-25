from typing import Callable, Optional, Union
from telegram.ext.dispatcher import DispatcherHandlerStop

from telegram import Message
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    MessageFilter,
    CallbackQueryHandler,
)
from telegram.ext.filters import DataDict

from . import adapters

def get_bot(token):
    updater = Updater(token, use_context=True)

    dp = updater.dispatcher

    # Добавляем роутер для динамических next_step_handlers
    dp.add_handler(
        MessageHandler(Filters.text, _next_step_router),
        group=-1,
    )

    return updater


def start(bot: Updater):
    bot.start_polling()
    bot.idle()


def register_command_handler(bot: Updater, handler: Callable, name: str, filter_function=None):  # pylint:disable=(unused-argument)
    dp = bot.dispatcher
    handler = adapters.prepare_handler(handler, bot)
    dp.add_handler(CommandHandler(name, handler))
    return bot

# Словарь для хранения следующих шагов
_next_steps = {}

def _next_step_router(update, context):
    chat_id = update.effective_chat.id

    if chat_id not in _next_steps:
        return

    handler = _next_steps.pop(chat_id)
    handler(update, context)
    raise DispatcherHandlerStop()


def register_next_step_handler(bot: Updater, chat, handler: Callable):
    handler = adapters.prepare_handler(handler, bot)
    _next_steps[chat.id] = handler
    return chat


def register_text_handler(bot: Updater, handler: Callable, text: str):
    return register_message_handler(bot, handler, lambda message: message.text == text)


def register_call_handler(
        bot: Updater,
        handler: Callable,
        call_data: str,
        filter_function: Callable = None  # pylint:disable=(unused-argument)
):
    """
    :param bot: Updater
    :param handler: функция-обработчик
    :param call_data: callback_data кнопки
    :param filter_function: -> bool для фильтрации
    """
    handler = adapters.prepare_call_handler(handler, bot)
    if filter_function is None:
        pattern = f'^{call_data}$'
    else:
        pattern = filter_function
    callback_handler = CallbackQueryHandler(handler, pattern=pattern)

    # Регистрируем handler
    bot.dispatcher.add_handler(callback_handler)

    return bot


def register_message_handler(
        bot: Updater,
        handler: Callable,
        filter_function: Callable = lambda message: True
    ):
    dp = bot.dispatcher
    handler = adapters.prepare_handler(handler, bot)

    class CurrentFilter(MessageFilter):

        def filter(self, message: Message) -> Optional[Union[bool, DataDict]]:  # pragma: no cover
            return filter_function(message)

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command & CurrentFilter(), handler))
    return bot


def get_commands_list(bot: Updater) -> list:
    dp = bot.dispatcher

    commands = []

    for group in dp.handlers.values():
        for handler in group:

            if isinstance(handler, CommandHandler):

                for command in handler.command:
                    commands.append(
                        (command, handler.callback)
                    )

    return commands
