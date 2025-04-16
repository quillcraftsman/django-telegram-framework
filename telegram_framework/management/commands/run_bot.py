from django.core.management.base import BaseCommand
from django.conf import settings
from telegram_framework import bots, links


class Command(BaseCommand):
    help = "Run telegram bot"

    def add_arguments(self, parser):
        parser.add_argument('--bot_links', type=str, default=settings.ROOT_BOT_LINKS)

    def handle(self, *args, **options):
        bot_links = options['bot_links']

        try:
            token = settings.TELEGRAM_BOT_TOKEN
        except AttributeError:
            token = '0'

        bot = bots.get_bot(token)
        bot_links = links.get_root_links(bot_links)
        links.add_links(bot, bot_links)
        bots.start(bot)
