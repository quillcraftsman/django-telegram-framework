from .functions import (
    get_last_response,
)


def test_start_command(client):
    """
    Test /commands: success
    """

    with client:
        _, text = get_last_response(client, '/commands')
        assert '/bot_father_commands' in text
        assert '/commands' in text
