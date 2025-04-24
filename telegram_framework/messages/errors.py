class MessageNotInChatError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'Нельзя ответить на сообщение "{self.message}", потому что оно не находиться в чате'
