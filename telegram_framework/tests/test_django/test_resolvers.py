from django.urls.resolvers import RoutePattern


def test_route_pattern_urls():
    pattern_str = '/admin/<int:param>/'
    current_path = '/admin/2/'
    route_pattern = RoutePattern(pattern_str)
    match = route_pattern.match(current_path)
    assert match is not None
    assert ('', (), {'param': 2}) == match


def test_route_pattern_text():
    pattern_str = 'admin <int:param> end'
    current_path = 'admin 2 end'
    route_pattern = RoutePattern(pattern_str)
    match = route_pattern.match(current_path)
    assert match is not None
    assert ('', (), {'param': 2}) == match


def test_just_test():
    pattern_str = 'some text'
    current_path = 'some text'
    route_pattern = RoutePattern(pattern_str)
    match = route_pattern.match(current_path)
    assert match is not None
    assert ('', (), {}) == match
    match = route_pattern.match('other text')
    assert match is None
