from dataclasses import dataclass
from typing import Any
from telegram_framework.messages import Message
from .image_base import ImageBase
from .image_default import ImageDefault



@dataclass(frozen=True)
class Image(ImageDefault, ImageBase):

    def __eq__(self, other):
        return (self.file_path == other.file_path
                and self.sender == other.sender
                and self.caption == other.caption)


def create_image(sender: Any, file_path: str, caption: Message = None):
    return Image(sender=sender, file_path=file_path, caption=caption)
