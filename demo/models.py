def create_info_text(command: str) -> str:
    text = (f'Привет. Я Demo Telegram Bot. '
            f'Я создан на основе Django Telegram Framework. '
            f'Я могу познакомить тебя с основными функциями библиотеки. '
            f'Например сейчас ты отправил команду {command} и видишь'
             f' это сообщение')
    return text


# class Faq(models.Model):
#     question = models.CharField(max_length=64, unique=True)
#     answer = models.CharField(max_length=128)


class Faq:

    class Objects:

        @staticmethod
        def all():
            queryset = [
                {
                    'question': 'Как быстрее писать код для списка',
                    'answer': 'Использовать list_action'
                },
                {
                    'question': 'Что это дает',
                    'answer': 'Можно ускорить разработку CRUD операций'
                }
            ]
            return queryset

    objects = Objects()
