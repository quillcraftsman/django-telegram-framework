from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Handler:
    function: Callable
    filter: Callable = lambda message: True


def create_handler(function, filter_function = lambda message: True):
    return Handler(
        function=function,
        filter=filter_function,
    )
