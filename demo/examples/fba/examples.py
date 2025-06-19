from telegram_framework import use
from demo.models import Faq


# START list_action_example
list_action_example = use.list_action(
    Faq,
    template_name='demo/bot/list.html',
)
# END list_action_example


# START list_action_pagination_example
list_action_pagination_example = use.list_action(
    Faq,
    template_name='demo/bot/list.html',
    pagination=use.list.Pagination(1, call_data_pattern='list_action_pagination {page}')
)
# END list_action_pagination_example


# START detail_action_example
detail_action_example = use.detail_action(
    Faq,
    'demo/bot/detail.html',
)
# END detail_action_example


# START template_action_example
template_action_example = use.template_action(
    'demo/bot/reply.html',
    context={
        'this': 'Это',
        'message': 'сообщение',
        'make': 'было создано по шаблону'
    }
)
# END template_action_example
