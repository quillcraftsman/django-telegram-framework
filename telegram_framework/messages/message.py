from dataclasses import dataclass
from .message_base import MessageBase
from .message_default import MessageDefault


@dataclass(frozen=True)
class Message(MessageDefault, MessageBase):

    def __eq__(self, other):
        return self.text == other.text and self.sender == other.sender


def create_message(text, sender, format_type='text'):
    return Message(text=text, sender=sender, format_type=format_type)
