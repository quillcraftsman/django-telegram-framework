from django.core.management.base import BaseCommand
from pygenesis_django.info import info


class Command(BaseCommand):
    help = "Pygenesis Django package info"

    def handle(self, *args, **options):

        self.stdout.write(
            self.style.SUCCESS(info())  # pylint: disable=no-member
        )
