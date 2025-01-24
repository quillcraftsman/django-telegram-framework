Быстрый старт
-------------

1. Создать django проект
2. Создать django приложение

.. code-block:: bash

    python manage.py startapp quickstart

3. В приложении создать файл `bot.py`
4. Пример кода в файле `bot.py`

.. literalinclude:: ../quickstart/bot.py
   :language: python

5. В `settings.py` проекта добавить следующие настройки:

.. code-block:: python

    TELEGRAM_BOT_TOKEN = '7777777777:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    TELEGRAM_BOT_TYPE = 'pyTelegramBotAPI'
    ROOT_BOT_LINKS = 'quickstart.bot'

6. Установить `pyTelegramBotAPI`

.. code-block:: bash

    pip install pyTelegramBotAPI

7. Запустить Бота

.. code-block:: bash

    python manage.py run_bot
