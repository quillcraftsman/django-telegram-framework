from pytest import fixture
from telegram_framework.test import asserts


@fixture
def bot_client():
    client = asserts.prepare_client()
    return client


@fixture
def chat(bot_client):  # pylint: disable=redefined-outer-name
    return asserts.prepare_chat(bot_client, 'demo.links')
