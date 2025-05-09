Все примеры
===========

Все примеры использования от простых к сложным.

- :ref:`links_py`
- :ref:`text_message`
- :ref:`html_message`
- :ref:`render_template`
- :ref:`echo_answer_example`
- :ref:`fixed_text_answer_example`
- :ref:`contains_text_answer_example`
- :ref:`send_picture`
- :ref:`send_picture_with_caption`
- :ref:`send_picture_with_html_caption`
- :ref:`message_with_inline_keyboard_example`
- :ref:`message_with_reply_keyboard_example`
- :ref:`get_user_id_example`
- :ref:`complex_message_example`


.. _links_py:
Файл links.py. Связи обработчиков для всех примеров ниже
--------------------------------------------------------

.. literalinclude:: ../demo/links.py
   :language: python

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

.. _fixed_text_answer_example:
Ответ на конкретное сообщение
-----------------------------

.. literalinclude:: ../demo/actions.py
   :language: python
   :start-after: START fixed_text_answer_example
   :end-before: END fixed_text_answer_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../demo/tests/test_commands.py
   :language: python
   :start-after: START test_fixed_text_answer_example
   :end-before: END test_fixed_text_answer_example

.. _contains_text_answer_example:
Ответ на сообщение содержащее текст
-----------------------------------

.. literalinclude:: ../demo/actions.py
   :language: python
   :start-after: START contains_text_answer_example
   :end-before: END contains_text_answer_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../demo/tests/test_commands.py
   :language: python
   :start-after: START test_contains_text_answer_example
   :end-before: END test_contains_text_answer_example

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


.. _message_with_reply_keyboard_example:
Клавиатура (Внизу чата)
-----------------------

.. literalinclude:: ../demo/actions.py
   :language: python
   :start-after: START message_with_reply_keyboard_example
   :end-before: END message_with_reply_keyboard_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../demo/tests/test_commands.py
   :language: python
   :start-after: START test_message_with_reply_keyboard_example
   :end-before: END test_message_with_reply_keyboard_example


.. _get_user_id_example:
Получение id пользователя
-------------------------

.. literalinclude:: ../demo/actions.py
   :language: python
   :start-after: START get_user_id_example
   :end-before: END get_user_id_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../demo/tests/test_commands.py
   :language: python
   :start-after: START test_get_user_id_example
   :end-before: END test_get_user_id_example


.. _complex_message_example:
Пример сложной логики
---------------------

.. literalinclude:: ../demo/actions.py
   :language: python
   :start-after: START complex_message_example
   :end-before: END complex_message_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../demo/tests/test_commands.py
   :language: python
   :start-after: START test_complex_message_example
   :end-before: END test_complex_message_example
