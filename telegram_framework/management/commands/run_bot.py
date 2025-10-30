from django.core.management.base import BaseCommand
from django.conf import settings
from telegram_framework import bots, links


class Command(BaseCommand):
    help = "Run telegram bot"

    def add_arguments(self, parser):
        parser.add_argument('--bot_links', type=str, default=settings.ROOT_BOT_LINKS)
        parser.add_argument('--bot_token_settings_name', type=str, default='TELEGRAM_BOT_TOKEN')

    def handle(self, *args, **options):
        bot_token_settings_name = options['bot_token_settings_name']
        try:
            token = getattr(settings, bot_token_settings_name)
        except AttributeError:
            token = '0'

        bot = bots.get_bot(token)
        bot_links = options['bot_links']
        bot_links = links.get_root_links(bot_links)
        links.add_links(bot, bot_links)
        bots.start(bot)
