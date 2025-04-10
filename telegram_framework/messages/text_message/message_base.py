from dataclasses import dataclass
from telegram_framework.messages.core import CoreMessageBase

@dataclass(frozen=True)
class MessageBase(CoreMessageBase):
    text: str
