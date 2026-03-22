import time
import os
from typing import Callable

from dotenv import load_dotenv
from pyrogram.types import Message
from pyrogram.types.messages_and_media.message import Str
from pyrogram import Client

load_dotenv()

bot_name = os.getenv('TELEGRAM_BOT_NAME')
default_timeout = float(os.getenv('DEFAULT_TIMEOUT', "0.5"))


def click_inline_button(
    client,
    message,
    callback_data,
    timeout=default_timeout,
) -> None:
    try:
        client.request_callback_answer(
            chat_id=message.chat.id,
            message_id=message.id,
            callback_data=callback_data,
            timeout=timeout,
        )
    except TimeoutError:
        # Если нет ответа на callback просто идем дальше
        pass


def _wait_answers(
        client,
        text,
        answers_count: int = 1,
        max_timeout: float = default_timeout,
) -> tuple[Message | None, Str | None]:
    current_timeout = 0.05  # сначала ждем 0.1 секунды
    client_messages_count = 1  # считаем, что клиент отправил 1 сообщение
    expected_count = answers_count + client_messages_count  # ожидаемое кол-во сообщений

    while True:
        # удваиваем timeout для очередной попытки
        current_timeout *= 2
        time.sleep(current_timeout)

        history = client.get_chat_history(bot_name)
        history_list = list(history)

        if current_timeout >= max_timeout:
            # Бот не отправил ответ
            raise AssertionError(
                f'Бот не ответил на сообщение: {text}'
            )
        if len(history_list) < expected_count:
            # Недостаточно сообщений, пробуем снова
            continue
        if len(history_list) >= expected_count:
            # Если история не пустая, там будет больше сообщений.
            # Проверяем сообщение клиента
            # 0 - ое сообщение - последнее в списке
            client_message_index = answers_count
            client_message: Message = history_list[client_message_index]
            if client_message.text != text:
                # Не то сообщение, пробуем снова
                continue
            # всё хорошо
            # берем последнее сообщение
            message: Message = history_list[0]
            return message, message.text


def send_message(
        client: Client,
        text: str,
    ) -> None:
    client.send_message(bot_name, text)


def get_last_response(
        client: Client,
        text: str,
        answers_count: int = 1,
        max_timeout: float = default_timeout,
    ) -> tuple[Message | None, Str | None]:
    send_message(client, text)

    return _wait_answers(
        client,
        text,
        answers_count,
        max_timeout,
    )


def check_response(
        client: Client,
        assert_function: Callable[[Message, Str], None],
        max_timeout: float = default_timeout
    ) -> None:
    current_timeout = 0.05  # сначала ждем 0.1 секунды
    min_chat_messages_count = 2  # минимальное ожидаемое кол-во сообщений

    while True:
        # удваиваем timeout для очередной попытки
        current_timeout *= 2
        time.sleep(current_timeout)

        history = client.get_chat_history(bot_name)
        history_list = list(history)
        history_list_length = len(history_list)

        if current_timeout >= max_timeout:
            # Бот не отправил ответ
            raise AssertionError(
                'Неправильный ответ от бота'
            )
        if history_list_length < min_chat_messages_count:
            # Недостаточно сообщений, пробуем снова
            continue
        if history_list_length >= min_chat_messages_count:
            # Если история не пустая, там будет больше сообщений.
            # берем последнее сообщение
            message: Message = history_list[0]
            # Надо по идее еще проверить отправителя, что это бот
            # Вдруг клиент отправил такое же сообщение
            # Пробуем применить к нему assert_function
            try:
                assert_function(message, message.text)
            except AssertionError:
                # пробуем снова пока не получиться
                # или не закончиться время
                continue
            else:
                # assert прошел выходим
                return


def clear_chat_history(client):
    while True:
        history = list(client.get_chat_history(bot_name, limit=100))
        if len(history) < 10:
            break
        ids = [msg.id for msg in history]
        client.delete_messages(bot_name, ids)
        time.sleep(0.1)
