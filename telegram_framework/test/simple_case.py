from django.test import SimpleTestCase as DjangoSimpleTestCase
from .base import TelegramFrameworkMixin


class SimpleTestCase(TelegramFrameworkMixin, DjangoSimpleTestCase):
    pass
