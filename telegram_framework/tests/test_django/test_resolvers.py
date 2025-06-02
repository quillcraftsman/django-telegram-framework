import unittest
from django.urls.resolvers import RoutePattern


class TestResolvers(unittest.TestCase):

    def test_route_pattern_urls(self):
        pattern_str = '/admin/<int:param>/'
        current_path = '/admin/2/'
        route_pattern = RoutePattern(pattern_str)
        match = route_pattern.match(current_path)
        self.assertIsNotNone(match)
        self.assertEqual(('', (), {'param': 2}), match)

    def test_route_pattern_text(self):
        pattern_str = 'admin <int:param> end'
        current_path = 'admin 2 end'
        route_pattern = RoutePattern(pattern_str)
        match = route_pattern.match(current_path)
        self.assertIsNotNone(match)
        self.assertEqual(('', (), {'param': 2}), match)

    def test_just_test(self):
        pattern_str = 'some text'
        current_path = 'some text'
        route_pattern = RoutePattern(pattern_str)
        match = route_pattern.match(current_path)
        self.assertIsNotNone(match)
        self.assertEqual(('', (), {}), match)
        match = route_pattern.match('other text')
        self.assertIsNone(match)
