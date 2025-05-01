from typing import List
from dataclasses import dataclass, field
from telegram_framework.functions import update


@dataclass(frozen=True)
class Keyboard:
    name: str
    buttons: List = field(default_factory=list)
    # layout: layouts.Layout = field(default_factory=layouts.default_layout)

    def __len__(self):
        return len(self.buttons)


def add_button(keyboard, button):
    new_buttons = keyboard.buttons + [button]
    return update(keyboard, buttons=new_buttons)


@dataclass(frozen=True)
class EmptyKeyboard:
    name: str = '-'


def add_buttons(keyboard, buttons):
    new_buttons = keyboard.buttons + buttons
    return update(keyboard, buttons=new_buttons)
