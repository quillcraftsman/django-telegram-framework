from django.core.management.base import BaseCommand
from telegram_framework.info import info


class Command(BaseCommand):
    help = "Django Telegram Framework package info"

    def handle(self, *args, **options):

        self.stdout.write(
            self.style.SUCCESS(info())  # pylint: disable=no-member
        )
