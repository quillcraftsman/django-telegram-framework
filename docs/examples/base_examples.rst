Базовое применение
==================

- :ref:`links`
- :ref:`text_message`
- :ref:`html_message`
- :ref:`render_template`
- :ref:`echo_answer_example`
- :ref:`fixed_text_answer_example`
- :ref:`contains_text_answer_example`
- :ref:`send_picture`
- :ref:`send_picture_with_caption`
- :ref:`send_picture_with_html_caption`
- :ref:`get_user_id_example`
- :ref:`send_param_text_message_example`
- :ref:`param_call_buttons_example`


.. _links:
Файл links.py. Связи обработчиков для всех примеров ниже
--------------------------------------------------------

.. literalinclude:: ../../demo/examples/base/links.py
   :language: python

.. _text_message:
Отправка текстового сообщения
-----------------------------

.. literalinclude:: ../../demo/examples/base/examples.py
   :language: python
   :start-after: START send_text_message_example
   :end-before: END send_text_message_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../../demo/tests/test_examples/test_base/test_links.py
   :language: python
   :start-after: START test_send_text_message_example
   :end-before: END test_send_text_message_example

.. _html_message:
Отправка текстового сообщения в формате HTML
--------------------------------------------

.. literalinclude:: ../../demo/examples/base/examples.py
   :language: python
   :start-after: START send_html_message_example
   :end-before: END send_html_message_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../../demo/tests/test_examples/test_base/test_links.py
   :language: python
   :start-after: START test_send_html_message_example
   :end-before: END test_send_html_message_example

.. _render_template:
Рендеринг шаблона в формате HTML
--------------------------------

.. literalinclude:: ../../demo/examples/base/examples.py
   :language: python
   :start-after: START render_template_example
   :end-before: END render_template_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../../demo/tests/test_examples/test_base/test_links.py
   :language: python
   :start-after: START test_render_template_example
   :end-before: END test_render_template_example

.. _echo_answer_example:
Отправка ответа на сообщение
----------------------------

.. literalinclude:: ../../demo/examples/base/examples.py
   :language: python
   :start-after: START echo_answer_example
   :end-before: END echo_answer_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../../demo/tests/test_examples/test_base/test_links.py
   :language: python
   :start-after: START test_echo_answer_example
   :end-before: END test_echo_answer_example

.. _fixed_text_answer_example:
Ответ на конкретное сообщение
-----------------------------

.. literalinclude:: ../../demo/examples/base/examples.py
   :language: python
   :start-after: START fixed_text_answer_example
   :end-before: END fixed_text_answer_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../../demo/tests/test_examples/test_base/test_links.py
   :language: python
   :start-after: START test_fixed_text_answer_example
   :end-before: END test_fixed_text_answer_example

.. _contains_text_answer_example:
Ответ на сообщение содержащее текст
-----------------------------------

.. literalinclude:: ../../demo/examples/base/examples.py
   :language: python
   :start-after: START contains_text_answer_example
   :end-before: END contains_text_answer_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../../demo/tests/test_examples/test_base/test_links.py
   :language: python
   :start-after: START test_contains_text_answer_example
   :end-before: END test_contains_text_answer_example

.. _send_picture:
Отправка изображения
--------------------

.. literalinclude:: ../../demo/examples/base/examples.py
   :language: python
   :start-after: START send_picture_example
   :end-before: END send_picture_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../../demo/tests/test_examples/test_base/test_links.py
   :language: python
   :start-after: START test_send_picture_example
   :end-before: END test_send_picture_example

.. _send_picture_with_caption:
Отправка изображения с заголовком
---------------------------------

.. literalinclude:: ../../demo/examples/base/examples.py
   :language: python
   :start-after: START send_picture_with_caption_example
   :end-before: END send_picture_with_caption_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../../demo/tests/test_examples/test_base/test_links.py
   :language: python
   :start-after: START test_send_picture_with_caption_example
   :end-before: END test_send_picture_with_caption_example

.. _send_picture_with_html_caption:
Отправка изображения с заголовком в формате HTML
------------------------------------------------

.. literalinclude:: ../../demo/examples/base/examples.py
   :language: python
   :start-after: START send_picture_with_html_caption_example
   :end-before: END send_picture_with_html_caption_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../../demo/tests/test_examples/test_base/test_links.py
   :language: python
   :start-after: START test_send_picture_with_html_caption_example
   :end-before: END test_send_picture_with_html_caption_example


.. _get_user_id_example:
Получение id пользователя
-------------------------

.. literalinclude:: ../../demo/examples/base/examples.py
   :language: python
   :start-after: START get_user_id_example
   :end-before: END get_user_id_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../../demo/tests/test_examples/test_base/test_links.py
   :language: python
   :start-after: START test_get_user_id_example
   :end-before: END test_get_user_id_example


.. _send_param_text_message_example:
Пример команды с параметром
---------------------------

.. literalinclude:: ../../demo/examples/base/examples.py
   :language: python
   :start-after: START send_param_text_message_example
   :end-before: END send_param_text_message_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../../demo/tests/test_examples/test_base/test_links.py
   :language: python
   :start-after: START test_send_param_text_message_example
   :end-before: END test_send_param_text_message_example

.. _param_call_buttons_example:
Пример вызова (call) с параметром
---------------------------------

.. literalinclude:: ../../demo/examples/base/examples.py
   :language: python
   :start-after: START param_call_buttons_example
   :end-before: END param_call_buttons_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../../demo/tests/test_examples/test_base/test_links.py
   :language: python
   :start-after: START test_param_call_buttons_example
   :end-before: END test_param_call_buttons_example
