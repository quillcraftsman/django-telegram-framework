from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class CoreMessageDefault:
    timestamp: datetime = field(default_factory=datetime.now)
