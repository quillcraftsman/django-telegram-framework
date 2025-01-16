from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from telegram_framework.chat import Chat


@dataclass(frozen=True)
class MessageDefault:
    timestamp: datetime = field(default_factory=datetime.now)
    chat: Optional[Chat] = None
