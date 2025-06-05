from dataclasses import dataclass
from django.core.paginator import Paginator
from telegram_framework.keyboards import inline, layouts


@dataclass(frozen=True)
class Pagination:
    paginate_by: int
    previous_button_name: str = '<<'
    next_button_name: str = '>>'
    call_data_pattern: str = 'list {page}'
    order_by: str = 'id'


def paginate(pagination: Pagination, input_queryset, page):
    # queryset
    ordered_queryset = input_queryset.order_by(pagination.order_by)
    paginator = Paginator(ordered_queryset, pagination.paginate_by)
    current_page = paginator.page(page)
    queryset = current_page.object_list

    # buttons
    buttons = []
    if current_page.has_previous():
        buttons.append(inline.Button(
            pagination.previous_button_name,
            pagination.call_data_pattern.format(page=current_page.previous_page_number())
        ))

    if current_page.has_next():
        buttons.append(
            inline.Button(
                pagination.next_button_name,
                pagination.call_data_pattern.format(page=current_page.next_page_number())
            )
        )

    columns_count = 2
    keyboard = inline.Keyboard(buttons=buttons, layout=layouts.Layout(columns_count))
    return queryset, keyboard
