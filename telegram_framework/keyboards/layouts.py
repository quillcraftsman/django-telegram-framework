from dataclasses import dataclass


@dataclass(frozen=True)
class Layout:
    columns_count: int = 1


def default_layout():
    return Layout()
