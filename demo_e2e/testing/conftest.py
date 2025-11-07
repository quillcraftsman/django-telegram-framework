import os
from dotenv import load_dotenv
from pyrogram import Client
from pytest import fixture
from .functions import clear_chat_history

load_dotenv()

api_id = os.getenv('CLIENT_API_ID')
api_hash = os.getenv('CLIENT_API_HASH')

@fixture(scope='session')
def client():
    result = Client(
        "kapitenlevantestclient",
        api_id,
        api_hash
    )
    with result:
        clear_chat_history(result)
    return result
