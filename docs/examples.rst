Все примеры
===========

Все примеры использования от простых к сложным

Проект на `GitHub <https://github.com/quillcraftsman/django-telegram-framework>`_

- :ref:`Отправка текстового сообщения`
- :ref:`Отправка текстового сообщения в формате HTML`
- :ref:`Рендеринг шаблона в формате HTML`
- :ref:`Отправка ответа на сообщение`
- :ref:`Отправка изображения`
- :ref:`Отправка изображения с заголовком`
- :ref:`Отправка изображения с заголовком в формате HTML`

Отправка текстового сообщения
-----------------------------

.. literalinclude:: ../demo/actions.py
   :language: python
   :start-after: START send_text_message_example
   :end-before: END send_text_message_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../demo/tests/test_commands.py
   :language: python
   :start-after: START test_send_text_message_example
   :end-before: END test_send_text_message_example

Отправка текстового сообщения в формате HTML
--------------------------------------------

.. literalinclude:: ../demo/actions.py
   :language: python
   :start-after: START send_html_message_example
   :end-before: END send_html_message_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../demo/tests/test_commands.py
   :language: python
   :start-after: START test_send_html_message_example
   :end-before: END test_send_html_message_example

Рендеринг шаблона в формате HTML
--------------------------------

Отправка ответа на сообщение
----------------------------

Отправка изображения
--------------------

Отправка изображения с заголовком
---------------------------------

Отправка изображения с заголовком в формате HTML
------------------------------------------------
