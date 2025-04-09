from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class MessageDefault:
    timestamp: datetime = field(default_factory=datetime.now)
    format_type: str = 'text'  # 'HTML'
