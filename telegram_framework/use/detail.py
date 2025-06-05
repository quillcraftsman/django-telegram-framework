from telegram_framework import messages, actions


def detail_action(
        model,
        template_name,
        context_object_name='object',
):

    def detail_action_result(bot, message, pk):
        current_object = model.objects.get(pk=pk)
        response = messages.create_template_message(
            bot,
            template_name,
            {
                context_object_name: current_object
            },
        )
        return actions.send_message(message.chat, response)

    return detail_action_result
