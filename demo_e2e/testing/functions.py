import time
import os
from dotenv import load_dotenv

load_dotenv()

bot_name = os.getenv('TELEGRAM_BOT_NAME')
default_timeout = float(os.getenv('DEFAULT_TIMEOUT', "0.5"))

def send_message(client, text):
    client.send_message(bot_name, text)

def click_inline_button(
    client,
    message,
    callback_data,
    timeout=default_timeout,
):
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


def wait_response(client, timeout=default_timeout):
    time.sleep(timeout)
    history = client.get_chat_history(bot_name, limit=1)
    message = list(history)[0]
    return message, message.text

def clear_chat_history(client):
    while True:
        history = list(client.get_chat_history(bot_name, limit=100))
        if len(history) < 10:
            break
        ids = [msg.id for msg in history]
        print('DELETE', ids)
        client.delete_messages(bot_name, ids)
        time.sleep(0.1)
        print('DONE')
