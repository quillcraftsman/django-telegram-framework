from .template import template_action


def list_action(
        model,
        template_name,
        context_object_name='objects_list',
        ):

    queryset = model.objects.all()
    context = {context_object_name: queryset}
    return template_action(template_name, context)
