from dataclasses import dataclass, field
from typing import List, Dict, Callable
from telegram_framework.functions import update


@dataclass(frozen=True)
class DummyBot:
    token: str
    command_handlers: Dict[str, Callable] = field(default_factory=dict)
    message_handlers: List[Callable] = field(default_factory=list)
    call_handlers: Dict[str, Callable] = field(default_factory=dict)


def register_command_handler(bot: DummyBot, handler: Callable, name: str):
    command_handlers = bot.command_handlers | {name: handler}
    return update(bot, command_handlers=command_handlers)
#
#
def register_message_handler(bot: DummyBot, handler: Callable):
    message_handlers = bot.message_handlers + [handler]
    return update(bot, message_handlers=message_handlers)

#
def register_call_handler(bot: DummyBot, handler: Callable, call_data):
    call_handlers = bot.call_handlers | {call_data: handler}
    return update(bot, call_handlers=call_handlers)


# def handle(bot: DummyBot)
# def find_handler(bot: DummyBot, message) -> Callable:
#     result = None
#     print('MESSAGE TEXT', message.text)
#     if message.text.startswith('/'):
#         # нашли команду
#         command_name = message.text.replace('/', '')
#         result = bot.commands.get(command_name, None)
#     return result
#
# def get_bot(api_token):
#     return DummyBot(api_token=api_token)
#
#
# def start(bot: DummyBot):
#     print('STARTED')
#     print(bot)
