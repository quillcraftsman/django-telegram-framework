from datetime import datetime
from dataclasses import dataclass, field
from typing import Any
from telegram_framework.messages import Message
from telegram_framework.messages.message_base import MessageToSend


@dataclass(frozen=True)
class Image(MessageToSend):
    file_path: str
    caption: Message = None
    timestamp: datetime = field(default_factory=datetime.now)


def create_image(sender: Any, file_path: str, caption: Message = None):
    return Image(sender=sender, file_path=file_path, caption=caption)
