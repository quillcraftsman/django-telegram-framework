from dataclasses import dataclass
from typing import Any
from .image_base import ImageBase
from .image_default import ImageDefault
from telegram_framework.messages import Message


@dataclass(frozen=True)
class Image(ImageDefault, ImageBase):
    pass


def create_image(sender: Any, file_path: str, caption: Message = None):
    return Image(sender=sender, file_path=file_path, caption=caption)