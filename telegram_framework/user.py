from dataclasses import dataclass


@dataclass(frozen=True)
class UserData:
    id: int
    first_name: str = None
    last_name: str = None
    username: str = None
