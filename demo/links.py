from telegram_framework import links
from . import actions

bot_links = links.include([], 'telegram_framework.commands.links')

bot_links += [
    links.on_command(actions.send_bot_info, 'start', 'Начать общение с ботом'),
    links.on_command(actions.send_bot_info, 'help', 'Получить информацию о боте'),
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
    links.on_command(
        actions.message_with_inline_keyboard_example,
        'message_with_inline_keyboard', 'Сообщение с кнопкой'
    ),
    # FBV (use)
    links.on_command(actions.list_action_example, 'list_action', 'Пример FBA CRUD List'),
    links.on_command(
        actions.list_action_pagination_example,
        'list_action_pagination',
        'Пример FBA CRUD List с Pagination'),
    links.on_call(actions.list_action_pagination_example,
                  'list_action_pagination',
                  params_pattern='list_action_pagination <int:page>'
                  ),
    links.on_command(
        actions.detail_action_example, 'detail_action',
        description_text='Пример FBA CRUD Detail',
        params_pattern='detail_action <int:pk>',
    ),
    links.on_command(
        actions.template_action_example,
        'template_action',
        'Пример FBA действия с шаблоном'
    ),
    links.on_command(
        actions.complex_message_example,
        'complex_message',
        'Пример всех функций в одном месте'
    ),
    links.on_text(actions.fixed_text_answer_example, 'Спасибо бот'),
    links.on_message(
        actions.contains_text_answer_example,
        lambda message: 'Привет' in message.text
    ),
    links.on_command(
        actions.message_with_reply_keyboard_example,
        'message_with_reply_keyboard',
        'Сообщение с клавиатурой',
    ),
    links.on_command(
        actions.get_user_id_example,
        'get_user_id',
        'Получение telegram id пользователя',
    ),
    links.on_command(
        actions.send_param_text_message_example,
        'param_text_message',
        'Отправка текстового сообщения с параметром',
        'param_text_message <str:param>',
    ),
    links.on_command(
        actions.param_call_buttons_example,
        'param_call_buttons',
        'Кнопки для обработчиков с параметрами',
    ),
    links.on_call(actions.put_button_param_handler,
                  'put_on_me_params',
                  params_pattern='put_on_me_params <str:param>'
                  ),
    links.on_command(
        actions.start_sequence_example,
        'sequence_example',
        'Последовательность ввода данных',
        # next_steps=[actions.sequence_last_name_example]
    ),
    links.on_text(actions.put_keyboard_handler, 'Нажми меня 🔍'),
    links.on_message(actions.echo_answer_example),
    links.on_call(actions.put_button_handler, 'put_on_me'),
]
