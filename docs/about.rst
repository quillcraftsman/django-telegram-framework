Django Telegram Framework
=========================

Библиотека (Framework) для быстрого создания **Telegram** ботов и интеграции с django

Проект на `GitHub <https://github.com/quillcraftsman/django-telegram-framework>`_

- :ref:`Идея проекта`
- :ref:`Проект с открытым исходным кодом`
- :ref:`Функции библиотеки`
- :ref:`Зависимости`
- :ref:`Статус разработки`

Идея проекта
------------

Создать удобный и надежный framework для быстрого и удобного создания telegram ботов который:

- models - модели данных связанные с базой данных с помощью Django ORM
- actions - обработчики событий telegram bot-а (аналогия с django views)
- links - связь команд и событий бота с обработчиками (аналогия с django urls)
- settings - настройки для всего проекта - django settings
- tests - тесты логики бота с использованием специального Dummy Bot

Проект с открытым исходным кодом
--------------------------------

Это проект с открытым исходным кодом с лицензией `Happy Code <https://github.com/quillcraftsman/django-telegram-framework/blob/main/LICENSE>`_.
- Свободное использование
- создание Forks
- публикация issues и bugs
- contributions
очень приветствуются

Функции библиотеки
------------------

- Интеграция telegram бота в django проект
- Понятная структура и интерфейсы для разработки бота
- Функции автоматического тестирования бота
- Совместимость с синхронным pyTelegramBotAPI
- Совместимость с асинхронным pyTelegramBotAPI (В разработке)
- DummyBot для тестирования и работы без подключения к telegram
- Функции телеграм бота (Будут добавляться по мере надобности, пожалуйста напишите, если вам нужна новая функция)
- Совместимость с aiogram, python-telegram-bot, Telethone (На этапе планирования)

Зависимости
-----------

.. include:: ../requirements.txt

Статус разработки
-----------------

- |project_name|

- |version|

- |development_status|

`Проект в PyPi <https://pypi.org/project/pygenesis-django>`_
