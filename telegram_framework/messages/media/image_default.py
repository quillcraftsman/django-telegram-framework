from dataclasses import dataclass
from telegram_framework.messages import Message
from telegram_framework.messages.core import CoreMessageDefault


@dataclass(frozen=True)
class ImageDefault(CoreMessageDefault):
    caption: Message = None
