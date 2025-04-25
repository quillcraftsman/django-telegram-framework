from dataclasses import dataclass
from typing import Any
from telegram_framework.messages.core import CoreMessageDefault
from .call_base import CallBase


@dataclass(frozen=True)
class Call(CoreMessageDefault, CallBase):
    pass


def create_call(sender: Any, data: str):
    return Call(
        sender, data
    )
