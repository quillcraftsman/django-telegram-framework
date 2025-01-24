def create_info_text(command: str) -> str:
    text = (f'Привет. Я Demo Telegram Bot. '
            f'Я создан на основе Django Telegram Framework. '
            f'Я могу познакомить тебя с основными функциями библиотеки. '
            f'Например сейчас ты отправил команду {command} и видишь'
             f' это сообщение')
    return text
