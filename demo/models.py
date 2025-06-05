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


class Queryset:

    def __init__(self):
        self.data = [
                {
                    'question': 'Как быстрее писать код для списка',
                    'answer': 'Использовать list_action'
                },
                {
                    'question': 'Что это дает',
                    'answer': 'Можно ускорить разработку CRUD операций'
                }
            ]

    def __getitem__(self, item):
        return self.data[item]

    def order_by(self, key):  # pylint: disable=unused-argument
        return self.data


class Faq:

    class Objects:

        @staticmethod
        def all():
            # queryset = [
            #     {
            #         'question': 'Как быстрее писать код для списка',
            #         'answer': 'Использовать list_action'
            #     },
            #     {
            #         'question': 'Что это дает',
            #         'answer': 'Можно ускорить разработку CRUD операций'
            #     }
            # ]
            queryset = Queryset()
            return queryset

        @staticmethod
        def get(pk):  # pylint: disable=unused-argument
            return {
                'question': 'Как быстрее писать код для списка',
                'answer': 'Использовать detail_action'
            }

    objects = Objects()
