import importlib
from django.core.management.base import BaseCommand
from django.conf import settings
from telegram_framework import get_bot, start
from telegram_framework.links import add_links


class Command(BaseCommand):
    help = "Run telegram bot"

    def handle(self, *args, **options):
        token = settings.TELEGRAM_BOT_TOKEN
        bot = get_bot(token)
        links_module = importlib.import_module('demo.links')
        add_links(bot, links_module.bot_links)
        start(bot)
