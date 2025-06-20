CRUD, FBA (FBV)
===============

Для ускорения разработки CRUD операций, удобно использовать готовые функции (По аналогии с CBV в Django).
Они находятся в модуле use и называются FBA (Functions Base Actions).

- :ref:`list_action`
- :ref:`list_action_pagination`
- :ref:`detail_action`
- :ref:`template_action`


.. _list_action:
Список элементов на основе шаблона
----------------------------------

.. literalinclude:: ../../demo/examples/fba/examples.py
   :language: python
   :start-after: START list_action_example
   :end-before: END list_action_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../../demo/tests/test_examples/test_fba/test_links.py
   :language: python
   :start-after: START test_list_action_example
   :end-before: END test_list_action_example


.. _list_action_pagination:
Список элементов на основе шаблона с пагинацией
-----------------------------------------------

.. literalinclude:: ../../demo/examples/fba/examples.py
   :language: python
   :start-after: START list_action_pagination_example
   :end-before: END list_action_pagination_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../../demo/tests/test_examples/test_fba/test_links.py
   :language: python
   :start-after: START test_list_action_pagination_example
   :end-before: END test_list_action_pagination_example


.. _detail_action:
Один элемент с pk на основе шаблона
-----------------------------------

.. literalinclude:: ../../demo/examples/fba/examples.py
   :language: python
   :start-after: START detail_action_example
   :end-before: END detail_action_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../../demo/tests/test_examples/test_fba/test_links.py
   :language: python
   :start-after: START test_detail_action_example
   :end-before: END test_detail_action_example


.. _template_action:
Сообщение на основе шаблона и контекста
---------------------------------------

.. literalinclude:: ../../demo/examples/fba/examples.py
   :language: python
   :start-after: START template_action
   :end-before: END template_action

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../../demo/tests/test_examples/test_fba/test_links.py
   :language: python
   :start-after: START test_template_action_example
   :end-before: END test_template_action_example
