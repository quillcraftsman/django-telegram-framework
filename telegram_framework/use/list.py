from telegram_framework import messages, actions
from .paginations import Pagination, paginate


def list_action(
        model,
        template_name,
        context_object_name='objects_list',
        pagination: Pagination = None,
        ):

    def list_action_result(bot, message, page=1):
        queryset = model.objects.all()
        keyboard = None
        if pagination:
            queryset, keyboard = paginate(pagination, queryset, page)

        context = {context_object_name: queryset}
        template_message = messages.create_template_message(
            sender=bot,
            template=template_name,
            context=context,
        )

        if keyboard:
            template_message = messages.add_keyboard(template_message, keyboard)

        return actions.send_message(message.chat, template_message)

    return list_action_result
