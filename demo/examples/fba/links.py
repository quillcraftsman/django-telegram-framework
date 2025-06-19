from telegram_framework import links
from . import examples


bot_links = [
    links.on_command(
        examples.list_action_example,
        'list_action',
        'Пример FBA CRUD List'
    ),
    links.on_command(
        examples.list_action_pagination_example,
        'list_action_pagination',
        'Пример FBA CRUD List с Pagination'
    ),
    links.on_call(
        examples.list_action_pagination_example,
        'list_action_pagination',
        params_pattern='list_action_pagination <int:page>'
    ),
    links.on_command(
        examples.detail_action_example, 'detail_action',
        description_text='Пример FBA CRUD Detail',
        params_pattern='detail_action <int:pk>',
    ),
    links.on_command(
        examples.template_action_example,
        'template_action',
        'Пример FBA действия с шаблоном'
    ),
]
