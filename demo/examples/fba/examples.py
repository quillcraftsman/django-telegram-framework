from telegram_framework import use, messages, chats, actions
from demo.models import Faq
from .forms import NameForm


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


# START create_action_example
def result_callback(bot, message):
    first_name = chats.get_note(message.chat, 'first_name', '?')
    last_name = chats.get_note(message.chat, 'last_name', '?')
    middle_name = chats.get_note(message.chat, 'middle_name', '?')
    result_text = f'Привет, {first_name} {last_name} {middle_name}'
    message_with_text = messages.create_message(result_text, sender=bot)
    chat = actions.send_message(message.chat, message_with_text)
    return chat


create_action_example = use.create_action(
    NameForm,
    result_callback,
)
# END create_action_example
