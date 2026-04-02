import pytest
from django.urls import reverse
from demo.models import create_info_text


def test_index_view(client):
    response = client.get(reverse('demo:index'))
    assert response.status_code == 200


def test_links_view(client):
    response = client.get(reverse('demo:links'))
    assert response.status_code == 200


@pytest.mark.parametrize('command', [
    'start',
    'help',
])
def test_command_view(client, command):
    response = client.get(reverse(f'demo:{command}'))
    assert response.status_code == 200
    context = response.context
    assert 'text' in context
    text = create_info_text(f'/{command}')
    assert context['text'] == text
