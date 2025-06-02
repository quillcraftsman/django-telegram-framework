from typing import Any
from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class CoreMessageDefault:
    timestamp: datetime = field(default_factory=datetime.now)
    chat: Any = None
    keyboard: Any = None
    message_id: int = None
