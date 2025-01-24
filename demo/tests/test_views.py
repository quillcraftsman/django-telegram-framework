from django.urls import reverse
from dry_tests import SimpleTestCase, Request, TrueResponse, Context
from demo.models import create_info_text


class TestIndexView(SimpleTestCase):

    def test_get(self):
        request = Request(reverse('demo:index'))
        true_response = TrueResponse(
            status_code=200,
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)


class TestCommandView(SimpleTestCase):

    def test_get(self):
        commands = ['start', 'help']
        for command in commands:
            with self.subTest(f'Test for /{command} command'):
                request = Request(reverse(f'demo:{command}'))
                text = create_info_text(f'/{command}')
                true_response = TrueResponse(
                    status_code=200,
                    context=Context(
                        items={'text': text}
                    ),
                    content_values=[text]
                )
                current_response = request.get_response(self.client)
                self.assertTrueResponse(current_response, true_response)


class TestLinksView(SimpleTestCase):

    def test_get(self):
        request = Request(reverse('demo:links'))
        true_response = TrueResponse(
            status_code=200,
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)