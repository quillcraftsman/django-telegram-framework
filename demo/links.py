from telegram_framework import links, commands
from . import actions


bot_links = [
    links.on_command(actions.send_bot_info, 'start', 'Начать общение с ботом'),
    links.on_command(actions.send_bot_info, 'help', 'Получить информацию о боте'),
    links.on_command(
        commands.get_commands,
        'commands',
        'Список примеров (что можно сделать с помощью DTF)'
    ),
    links.on_command(
        actions.send_text_message_example,
        'text_message',
        'Отправка текстового сообщения'
    ),
    links.on_command(actions.send_html_message_example, 'html_message', 'Отправка html сообщения'),
    links.on_command(
        actions.render_template_example,
        'render_template',
        'Форматирование по шаблону'
    ),
    links.on_command(actions.send_picture_example, 'send_picture', 'Отправка картинки'),
    links.on_command(
        actions.send_picture_with_caption_example,
        'send_picture_with_caption',
        'Отправка картинки с заголовком'
    ),
    links.on_command(
        actions.send_picture_with_html_caption_example,
        'send_picture_with_html_caption', 'Отправка картинки с HTML заголовком'
    ),
    # FBV (use)
    links.on_command(actions.list_action_example, 'list_action', 'Пример FBA CRUD List'),
    links.on_command(
        actions.template_action_example,
        'template_action',
        'Пример FBA действия с шаблоном'
    ),
    links.on_message(actions.echo_answer_example),
]
