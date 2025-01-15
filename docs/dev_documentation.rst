Документация для разработчиков
------------------------------

Установка зависимостей
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    pip install -r requirements.txt
    pip install -r dev-requirements.txt
    pip install -r doc-requirements.txt

Makefile
^^^^^^^^

Думаю будет полезно проверить **Makefile**. Он содержит основные полезные команды для разработки проекта:

.. include:: ../Makefile

С чего начать
^^^^^^^^^^^^^

Вы можете начать с запуска тестов и покрытия (coverage):

.. code-block:: shell

    make coverage
    make test

Пожалуйста запустите linter перед отправкой pull-request

.. code-block:: shell

    make lint

Сборка документации
^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    make package_docs
    cd docs
    make clean html
    make html
