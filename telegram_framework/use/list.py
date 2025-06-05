from django.core.paginator import Paginator
from telegram_framework import messages, actions
from telegram_framework.keyboards import inline, layouts
from .paginations import Pagination


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
            # queryset
            paginator = Paginator(queryset, pagination.paginate_by)
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

            keyboard = inline.Keyboard(buttons=buttons, layout=layouts.Layout(2))

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
