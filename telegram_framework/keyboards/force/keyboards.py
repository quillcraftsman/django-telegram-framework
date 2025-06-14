from dataclasses import dataclass


@dataclass(frozen=True)
class Keyboard:
    selective: bool = True
