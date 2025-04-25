Все примеры
===========

Все примеры использования от простых к сложным


- :ref:`text_message`
- :ref:`html_message`
- :ref:`render_template`
- :ref:`echo_answer_example`
- :ref:`send_picture`
- :ref:`send_picture_with_caption`
- :ref:`send_picture_with_html_caption`
- :ref:`message_with_inline_keyboard_example`


.. _text_message:
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

.. _html_message:
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

.. _render_template:
Рендеринг шаблона в формате HTML
--------------------------------

.. literalinclude:: ../demo/actions.py
   :language: python
   :start-after: START render_template_example
   :end-before: END render_template_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../demo/tests/test_commands.py
   :language: python
   :start-after: START test_render_template_example
   :end-before: END test_render_template_example

.. _echo_answer_example:
Отправка ответа на сообщение
----------------------------

.. literalinclude:: ../demo/actions.py
   :language: python
   :start-after: START echo_answer_example
   :end-before: END echo_answer_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../demo/tests/test_commands.py
   :language: python
   :start-after: START test_echo_answer_example
   :end-before: END test_echo_answer_example

.. _send_picture:
Отправка изображения
--------------------

.. literalinclude:: ../demo/actions.py
   :language: python
   :start-after: START send_picture_example
   :end-before: END send_picture_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../demo/tests/test_commands.py
   :language: python
   :start-after: START test_send_picture_example
   :end-before: END test_send_picture_example

.. _send_picture_with_caption:
Отправка изображения с заголовком
---------------------------------

.. literalinclude:: ../demo/actions.py
   :language: python
   :start-after: START send_picture_with_caption_example
   :end-before: END send_picture_with_caption_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../demo/tests/test_commands.py
   :language: python
   :start-after: START test_send_picture_with_caption_example
   :end-before: END test_send_picture_with_caption_example

.. _send_picture_with_html_caption:
Отправка изображения с заголовком в формате HTML
------------------------------------------------

.. literalinclude:: ../demo/actions.py
   :language: python
   :start-after: START send_picture_with_html_caption_example
   :end-before: END send_picture_with_html_caption_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../demo/tests/test_commands.py
   :language: python
   :start-after: START test_send_picture_with_html_caption_example
   :end-before: END test_send_picture_with_html_caption_example


.. _message_with_inline_keyboard_example:
Встроенная кнопка
-----------------

.. literalinclude:: ../demo/actions.py
   :language: python
   :start-after: START message_with_inline_keyboard_example
   :end-before: END message_with_inline_keyboard_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../demo/tests/test_commands.py
   :language: python
   :start-after: START test_message_with_inline_keyboard_example
   :end-before: END test_message_with_inline_keyboard_example
