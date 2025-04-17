from telegram_framework import messages, actions


def list_action(
        model,
        template_name,
        context_object_name='objects_list',
        ):

    def list_action_result(bot, message):
        queryset = model.objects.all()
        list_message = messages.create_template_message(
            template=template_name,
            context={context_object_name: queryset},
            sender=bot,
        )
        return actions.send_message(message.chat, list_message)

    return list_action_result
