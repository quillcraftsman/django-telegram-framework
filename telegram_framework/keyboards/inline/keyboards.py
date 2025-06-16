from typing import List
from dataclasses import dataclass, field, replace
from telegram_framework.keyboards import layouts


@dataclass(frozen=True)
class Keyboard:
    buttons: List = field(default_factory=list)
    layout: layouts.Layout = field(default_factory=layouts.default_layout)

    def __len__(self):
        return len(self.buttons)


def add_button(keyboard, button):
    new_buttons = keyboard.buttons + [button]
    return replace(keyboard, buttons=new_buttons)


def add_buttons(keyboard, buttons):
    new_buttons = keyboard.buttons + buttons
    return replace(keyboard, buttons=new_buttons)
