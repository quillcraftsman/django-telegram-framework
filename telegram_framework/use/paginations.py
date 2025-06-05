from dataclasses import dataclass


@dataclass(frozen=True)
class Pagination:
    paginate_by: int
    previous_button_name: str = '<<'
    next_button_name: str = '>>'
    call_data_pattern: str = 'list {page}'
