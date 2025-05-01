from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Handler:
    function: Callable
    filter: Callable = lambda message: True
    description: str = None


def create_handler(function, filter_function = lambda message: True, description=None):
    return Handler(
        function=function,
        filter=filter_function,
        description=description if description else function.__name__
    )
