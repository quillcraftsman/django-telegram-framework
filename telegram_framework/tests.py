"""
Tests
"""
from django.test import TestCase, Client
from django.core.management import call_command
from django.apps import apps
from django.conf import settings
from .info import info

class TestInfo(TestCase):
    """
    TestInfo TestCase
    """
    def setUp(self):
        """
        setUp test data
        """
        self.client = Client()

    def test_info_text(self):
        """
        Test info_text: success
        """
        result = 'Django Telegram Framework'
        self.assertEqual(result, info())

    def test_django_configuration(self):
        """
        Test django configuration
        """
        self.assertTrue(apps.is_installed('telegram_framework'))
        self.assertIn('django.contrib.admin', settings.INSTALLED_APPS)
        self.assertIn('django.contrib.auth', settings.INSTALLED_APPS)
        self.assertIn('django.contrib.contenttypes', settings.INSTALLED_APPS)
        call_command('check')
