from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Django Telegram Framework package info"

    def handle(self, *args, **options):

        self.stdout.write(
            self.style.SUCCESS('It works')  # pylint: disable=no-member
        )
