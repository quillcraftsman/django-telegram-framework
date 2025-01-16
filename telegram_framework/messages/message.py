from dataclasses import dataclass
from .message_base import MessageBase
from .message_default import MessageDefault


@dataclass(frozen=True)
class Message(MessageDefault, MessageBase):
    pass
