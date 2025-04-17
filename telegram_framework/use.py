from telegram_framework import messages, actions


def template_action(
        template_name,
        context=None,
):

    def template_action_result(bot, message):
        template_message = messages.create_template_message(
            sender=bot,
            template=template_name,
            context=context,
        )
        return actions.send_message(message.chat, template_message)

    return template_action_result


def list_action(
        model,
        template_name,
        context_object_name='objects_list',
        ):

    queryset = model.objects.all()
    context = {context_object_name: queryset}
    return template_action(template_name, context)
