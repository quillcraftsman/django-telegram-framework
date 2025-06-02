from dataclasses import dataclass
from django.template.loader import render_to_string
from .message_base import MessageBase
from .message_default import MessageDefault


@dataclass(frozen=True)
class Message(MessageDefault, MessageBase):

    def __eq__(self, other):
        return self.text == other.text and self.sender == other.sender

    def __str__(self):
        return self.text


def create_message(text, sender, format_type='text', message_id=None):
    return Message(text=text, sender=sender, format_type=format_type, message_id=message_id)


def create_template_message(sender, template, context=None, format_type='HTML'):
    text = render_to_string(template, context)
    return create_message(text, sender, format_type)
