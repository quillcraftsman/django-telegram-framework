from django.test import TestCase as DjangoTestCase  # pragma: no cover
from .base import TelegramFrameworkMixin  # pragma: no cover

class TestCase(TelegramFrameworkMixin, DjangoTestCase):  # pragma: no cover
    pass
