Тестирование
------------

Django Telegram Framework позволяет удобно тестировать код бота без подключения к telegram.
Для этого используется специальный `DummyBot`

1. В `settings.py` проекта внесите следующие изменения:

.. code-block:: python

    TELEGRAM_BOT_TOKEN = '0'
    TELEGRAM_BOT_TYPE = 'Dummy'

2. Пример написания тестов для бота из `quickstart` приложения

.. literalinclude:: ../quickstart/tests.py
   :language: python

3. Запустить django тесты

.. code-block:: bash

    python manage.py test
