# Django Telegram Framework

Библиотека (Framework) для быстрого создания **Telegram** ботов и интеграции с django

<img src="logo_2_1_1280_640.png" alt="Django Telegram Framework logo" width="50%">

[Тут][documentation_path] можно найти **Полную документацию проекта** 

<hr>

#### Workflows
[![Tests](https://github.com/quillcraftsman/django-telegram-framework/actions/workflows/run-tests.yml/badge.svg?branch=main)](https://github.com/quillcraftsman/django-telegram-framework/actions/workflows/run-tests.yml)
[![Pylint](https://github.com/quillcraftsman/django-telegram-framework/actions/workflows/lint.yml/badge.svg?branch=main)](https://github.com/quillcraftsman/django-telegram-framework/actions/workflows/lint.yml)

#### Package
[![Version](https://img.shields.io/pypi/v/django-telegram-framework.svg)](https://pypi.python.org/pypi/django-telegram-framework/)
[![Development Status](https://img.shields.io/pypi/status/django-telegram-framework.svg)](https://pypi.python.org/pypi/django-telegram-framework)
[![Python version](https://img.shields.io/pypi/pyversions/django-telegram-framework.svg)](https://pypi.python.org/pypi/django-telegram-framework/)
[![License](https://img.shields.io/pypi/l/django-telegram-framework)](https://github.com/quillcraftsman/django-telegram-framework/blob/main/LICENSE)
[![Wheel](https://img.shields.io/pypi/wheel/django-telegram-framework.svg)](https://pypi.python.org/pypi/django-telegram-framework/)

#### Support
[![Documentation](https://img.shields.io/badge/docs-0094FF.svg)][documentation_path]
[![Discussions](https://img.shields.io/badge/discussions-ff0068.svg)](https://github.com/quillcraftsman/django-telegram-framework/discussions/)
[![Issues](https://img.shields.io/badge/issues-11AE13.svg)](https://github.com/quillcraftsman/django-telegram-framework/issues/)

#### Downloads
[![Day Downloads](https://img.shields.io/pypi/dd/django-telegram-framework)](https://pepy.tech/project/django-telegram-framework)
[![Week Downloads](https://img.shields.io/pypi/dw/django-telegram-framework)](https://pepy.tech/project/django-telegram-framework)
[![Month Downloads](https://img.shields.io/pypi/dm/django-telegram-framework)](https://pepy.tech/project/django-telegram-framework)
[![All Downloads](https://img.shields.io/pepy/dt/django-telegram-framework)](https://pepy.tech/project/django-telegram-framework)

#### Languages
[![Languages](https://img.shields.io/github/languages/count/quillcraftsman/django-telegram-framework)](https://github.com/quillcraftsman/django-telegram-framework)
[![Top Language](https://img.shields.io/github/languages/top/quillcraftsman/django-telegram-framework)](https://github.com/quillcraftsman/django-telegram-framework)

#### Development
- [![Release date](https://img.shields.io/github/release-date/quillcraftsman/django-telegram-framework
)](https://github.com/quillcraftsman/django-telegram-framework/releases)
[![Last Commit](https://img.shields.io/github/last-commit/quillcraftsman/django-telegram-framework/main
)](https://github.com/quillcraftsman/django-telegram-framework)
- [![Issues](https://img.shields.io/github/issues/quillcraftsman/django-telegram-framework
)](https://github.com/quillcraftsman/django-telegram-framework/issues/)
[![Closed Issues](https://img.shields.io/github/issues-closed/quillcraftsman/django-telegram-framework
)](https://github.com/quillcraftsman/django-telegram-framework/issues/)
- [![Pull Requests](https://img.shields.io/github/issues-pr/quillcraftsman/django-telegram-framework
)](https://github.com/quillcraftsman/django-telegram-framework/pulls)
[![Closed Pull Requests](https://img.shields.io/github/issues-pr-closed-raw/quillcraftsman/django-telegram-framework
)](https://github.com/quillcraftsman/django-telegram-framework/pulls)
- [![Discussions](https://img.shields.io/github/discussions/quillcraftsman/django-telegram-framework
)](https://github.com/quillcraftsman/django-telegram-framework/discussions/)

[//]: # (#### Repository Stats)

[//]: # ([![Stars]&#40;https://img.shields.io/github/stars/quillcraftsman/django-telegram-framework)

[//]: # (&#41;]&#40;https://github.com/quillcraftsman/django-telegram-framework&#41;)

[//]: # ([![Contributors]&#40;https://img.shields.io/github/contributors/quillcraftsman/django-telegram-framework)

[//]: # (&#41;]&#40;https://github.com/quillcraftsman/django-telegram-frameworkgraphs/contributors&#41;)

[//]: # ([![Forks]&#40;https://img.shields.io/github/forks/quillcraftsman/django-telegram-framework)

[//]: # (&#41;]&#40;https://github.com/quillcraftsman/django-telegram-framework&#41;)

<hr>

## Menu

- [Идея проекта](#идея-проекта)
- [Проект с открытым исходным кодом](#проект-с-открытым-исходным-кодом)
- [Отличие от других Telegram проектов](#отличие-от-других-telegram-проектов)
- [Функции библиотеки](#функции-библиотеки)
- [Зависимости](#зависимости)
- [Статус разработки](#статус-разработки)
- [Установка](#установка)
- [Быстрый старт](#быстрый-старт)
- [Тестирование](#тестирование)
- [Внести свой вклад в проект](#внести-свой-вклад-в-проект)

## Идея проекта

Создать удобный и надежный framework для быстрого и удобного создания telegram ботов который:

- Имеет чёткую структуру модулей
- Может использовать разные библиотеки для взаимодействия с telegram (pyTelegramBotAPI, Telethone, python-telegram-bot, aiogram и другие)
- Позволяет быстро реализовать start-up проект одному разработчику или в небольшой команде
- Имеет интеграцию с django для создания web страниц и использования django admin
- Быстро подключается к базе данных с помощью Django ORM

## Проект с открытым исходным кодом

Это проект с открытым исходным кодом с лицензией [Happy Code](LICENSE). 

- Свободное использование
- создание Forks
- публикация issues и bugs
- contributions

очень приветствуются

## Отличие от других Telegram проектов
В отличие от библиотек для создания telegram ботов, таких как pyTelegramBotAPI, aiogram, python-telegram-bot и других,
этот проект (Framework) имеет чёткую структуру, похожую на структуру django проектов. Framework содержит следующие элементы:

- models - модели данных связанные с базой данных с помощью Django ORM
- actions - обработчики событий telegram bot-а (аналогия с django views)
- links - связь команд и событий бота с обработчиками (аналогия с django urls)
- settings - настройки для всего проекта - django settings
- tests - тесты логики бота с использованием специального Dummy Bot

Под капотом Framework может использовать разные библиотеки в синхронном и асинхронном исполнении. Можно переключать одни библиотеки на другие.
Без соединения с telegram (например в DEV) режиме, можно использовать Dummy Bot для разработки и тестирования.

Интеграция с django позволяет:
- Добавить web site
- Использовать django админку
- Использовать django ORM

## Функции библиотеки

- Интеграция telegram бота в django проект
- Понятная структура и интерфейсы для разработки бота
- Функции автоматического тестирования бота
- Совместимость с синхронным pyTelegramBotAPI
- Совместимость с асинхронным pyTelegramBotAPI (В разработке)
- DummyBot для тестирования и работы без подключения к telegram
- Функции телеграм бота (Будут добавляться по мере надобности, пожалуйста напишите, если вам нужна новая функция)
- Совместимость с aiogram, python-telegram-bot, Telethone (На этапе планирования)

## Зависимости

- django > 5
- pyTelegramBotAPi (Нужно установить отдельно)
- Подробности в [Полной документации](https://quillcraftsman.github.io/django-telegram-framework/about.html#requirements)

## Статус разработки

Написана и проверена 2-ая сырая версия библиотеки с небольшим набором функций

- Пакет уже доступен в [PyPi](https://pypi.org/project/django-telegram-framework/)
- Подробности в [Полной документации](https://quillcraftsman.github.io/django-telegram-framework/about.html#development-status)

## Установка

### with pip

```commandline
pip install django-telegram-framework
```

Подробности в [Полной документации](https://quillcraftsman.github.io/django-telegram-framework/install.html)

## Быстрый старт

0. Добавить `telegram_framework` в `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    '...',
    'telegram_framework',
    '...',
]
```

1. Создать django проект
2. Создать django приложение

```commandline
python manage.py startapp quickstart
```

3. В приложении создать файл `bot.py`
4. Пример кода в файле `bot.py`

```python
from telegram_framework import (
    messages,
    actions,
    links,
)
# ОПИШИТЕ ОБРАБОТЧИКИ СОБЫТИЙ БОТА

def send_greetings(bot, message):
    # Используйте специальный тип для сообщений
    greetings_message = messages.create_message(
        'Приветствую тебя. Я Quickstart Telegram Bot',
        sender=bot
    )
    # Отправьте сообщение в телеграмм
    return actions.send_message(message.chat, greetings_message)

def reply_to_message(bot, message):
    # Используйте специальную функцию для создания ответа
    reply = messages.create_reply(message, 'Тебе отвечает Bot', sender=bot)
    # Отправьте ответ в телеграмм
    return actions.send_reply(reply)


# СВЯЖИТЕ ОБРАБОТЧИКИ С ДЕЙСТВИЯМИ ПОЛЬЗОВАТЕЛЯ В TELEGRAM

bot_links = [
    links.on_command(send_greetings, 'start'),
    links.on_command(send_greetings, 'help'),
    links.on_message(reply_to_message),
]

```

5. В `settings.py` проекта добавить следующие настройки:

```python
TELEGRAM_BOT_TOKEN = '7777777777:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
TELEGRAM_BOT_TYPE = 'pyTelegramBotAPI'
ROOT_BOT_LINKS = 'quickstart.bot'
```

6. Установить `pyTelegramBotAPI`

```commandline
pip install pyTelegramBotAPI
```

7. Запустить Бота

```commandline
python manage.py run_bot
```

### Больше примеров в [Полной документации][documentation_path]

## Тестирование

Django Telegram Framework позволяет удобно тестировать код бота без подключения к telegram.
Для этого используется специальный `DummyBot`

1. В `settings.py` проекта внесите следующие изменения:

```python
TELEGRAM_BOT_TOKEN = '0'
TELEGRAM_BOT_TYPE = 'Dummy'
```

2. Пример написания тестов для бота из `quickstart` приложения

```python
from telegram_framework.test import SimpleTestCase


class TestCommands(SimpleTestCase):

    def test_start(self):
        """
        Test /start: success
        """
        # Бот должен реагировать на сообщения
        chat = self.assertCommandWasHandled('/start', self.chat)
        # Последнее сообщение в чате должно содержать приветствие
        self.assertChatLastMessageTextEqual(chat, 'Приветствую тебя. Я Quickstart Telegram Bot')


    def test_any_text_message(self):
        """
        Test send any text message: success
        """
        # Бот должен реагировать на сообщение,
        chat = self.assertTextMessageWasHandled('quickstart message', self.chat)
        # Последнее сообщение должно содержать ответ бота
        self.assertChatLastMessageTextEqual(chat, 'Тебе отвечает Bot')
```

3. Запустить django тесты

```commandline
python manage.py test
```

## Внести свой вклад в проект

Без проблем! Для быстрого старта можно ознакомиться с:
- [Полной документацией][documentation_path]
- [Как внести свой вклад](CONTRIBUTING.md)
- [Документацией для разработчиков](https://quillcraftsman.github.io/django-telegram-framework/dev_documentation.html)
- [Нормами поведения](CODE_OF_CONDUCT.md)
- [Политикой безопасности](SECURITY.md)
- [Структурой управления проектом](GOVERNANCE.md)
- [Файлом поддержки](SUPPORT.md)

[documentation_path]: https://quillcraftsman.github.io/django-telegram-framework
