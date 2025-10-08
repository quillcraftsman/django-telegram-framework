from telegram_framework import links
from . import examples


bot_links = [
    links.on_command(
        examples.send_text_message_example,
        'text_message',
        'Отправка текстового сообщения'
    ),
    links.on_command(
        examples.send_html_message_example,
        'html_message',
        'Отправка html сообщения'
    ),
    links.on_command(
        examples.render_template_example,
        'render_template',
        'Форматирование по шаблону'
    ),
    links.on_command(
        examples.send_picture_example,
        'send_picture',
        'Отправка картинки'
    ),
    links.on_command(
        examples.send_picture_with_caption_example,
        'send_picture_with_caption',
        'Отправка картинки с заголовком'
    ),
    links.on_command(
        examples.send_picture_with_html_caption_example,
        'send_picture_with_html_caption',
        'Отправка картинки с HTML заголовком'
    ),
    links.on_text(
        examples.fixed_text_answer_example,
        'Спасибо бот'
    ),
    links.on_message(
        examples.contains_text_answer_example,
        lambda message: 'Привет' in message.text
    ),
    links.on_command(
        examples.get_user_data_example,
        'get_user_data',
        'Получение telegram id пользователя',
    ),
    links.on_command(
        examples.send_param_text_message_example,
        'param_text_message',
        'Отправка текстового сообщения с параметром',
        'param_text_message <str:param>',
    ),
    links.on_command(
        examples.param_call_buttons_example,
        'param_call_buttons',
        'Кнопки для обработчиков с параметрами',
    ),
    links.on_call(
        examples.put_button_param_handler,
        'put_on_me_params',
        params_pattern='put_on_me_params <str:param>'
    ),
    links.on_message(examples.echo_answer_example),
]
