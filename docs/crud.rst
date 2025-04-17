CRUD, FBA (FBV)
===============

Для ускорения разработки CRUD операция удобно использовать готовые функции (По аналогии с CBV в Django).
Они находятся в модуле use и называются FBA (Functions Base Actions).

- :ref:`list_action`


.. _list_action:
Список элементов на основе шаблона
----------------------------------

.. literalinclude:: ../demo/actions.py
   :language: python
   :start-after: START list_action_example
   :end-before: END list_action_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../demo/tests/test_commands.py
   :language: python
   :start-after: START test_list_action_example
   :end-before: END test_list_action_example
