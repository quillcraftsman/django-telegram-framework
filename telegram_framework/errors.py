class BotTypeError(ValueError):

    def __init__(self, bot_type):
        self.bot_type = bot_type

    def __str__(self):
        return f'Unknown BOT_TYPE: {self.bot_type}'
