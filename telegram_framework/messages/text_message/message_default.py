from dataclasses import dataclass
from telegram_framework.messages.core.core_message_default import CoreMessageDefault


@dataclass(frozen=True)
class MessageDefault(CoreMessageDefault):
    format_type: str = 'text'  # 'HTML'
