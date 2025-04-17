import functools

DESCRIPTION_ATTRIBUTE = '__dtf_description__'


def set_description(handler, text):
    setattr(handler, DESCRIPTION_ATTRIBUTE, text)


def get_description(handler):
    return getattr(handler, DESCRIPTION_ATTRIBUTE) \
        if hasattr(handler, DESCRIPTION_ATTRIBUTE) \
        else handler.__name__


def description(text):

    def decorator(handler):

        @functools.wraps(handler)
        def wrapper(*args, **kwargs):
            return handler(*args, **kwargs)

        set_description(wrapper, text)
        return wrapper

    return decorator
