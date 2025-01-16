from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Any



@dataclass(frozen=True)
class MessageDefault:
    timestamp: datetime = field(default_factory=datetime.now)
    chat: Optional[Any] = None
