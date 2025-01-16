from dataclasses import dataclass
from .message_default import MessageDefault
from .reply_base import ReplyBase


@dataclass(frozen=True)
class Reply(MessageDefault, ReplyBase):
    pass
