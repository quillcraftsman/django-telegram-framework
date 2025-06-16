from typing import List
from dataclasses import dataclass, field, replace


@dataclass(frozen=True)
class Keyboard:
    name: str
    buttons: List = field(default_factory=list)
    # layout: layouts.Layout = field(default_factory=layouts.default_layout)

    def __len__(self):
        return len(self.buttons)

    def __str__(self):
        return self.name


def add_button(keyboard, button):
    new_buttons = keyboard.buttons + [button]
    return replace(keyboard, buttons=new_buttons)


@dataclass(frozen=True)
class EmptyKeyboard:
    name: str = '-'


def add_buttons(keyboard, buttons):
    new_buttons = keyboard.buttons + buttons
    return replace(keyboard, buttons=new_buttons)
