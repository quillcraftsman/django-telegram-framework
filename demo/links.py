from telegram_framework import links
from . import actions


bot_links = [
    links.on_command(actions.send_bot_info, 'start'),
    links.on_command(actions.send_bot_info, 'help'),
    links.on_command(actions.commands_info, 'commands'),
    links.on_command(actions.send_text_message_example, 'text_message'),
    links.on_command(actions.send_html_message_example, 'html_message'),
    links.on_command(actions.render_template_example, 'render_template'),
    links.on_command(actions.send_picture_example, 'send_picture'),
    links.on_command(actions.send_picture_with_caption_example, 'send_picture_with_caption'),
    links.on_command(
        actions.send_picture_with_html_caption_example,
        'send_picture_with_html_caption'
    ),
    # FBV (use)
    links.on_command(actions.list_action_example, 'list_action'),
    links.on_command(actions.template_action_example, 'template_action'),
    links.on_message(actions.echo_answer_example),
]
