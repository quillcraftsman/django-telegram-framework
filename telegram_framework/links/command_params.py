from django.urls.resolvers import RoutePattern


def _match_function(message, pattern):
    route_pattern = RoutePattern(f'/{pattern}')
    return route_pattern.match(message.text)


def get_match_function(pattern):

    def inner(message):
        return _match_function(message, pattern)

    return inner
