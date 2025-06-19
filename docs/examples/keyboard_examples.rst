Использование клавиатуры
========================

- :ref:`links`
- :ref:`message_with_inline_keyboard_example`
- :ref:`message_with_reply_keyboard_example`

.. _links:
Файл links.py. Связи обработчиков для всех примеров ниже
--------------------------------------------------------

.. literalinclude:: ../../demo/examples/keyboard/links.py
   :language: python

.. _message_with_inline_keyboard_example:
Встроенная кнопка
-----------------

.. literalinclude:: ../../demo/examples/keyboard/examples.py
   :language: python
   :start-after: START message_with_inline_keyboard_example
   :end-before: END message_with_inline_keyboard_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../../demo/tests/test_examples/test_keyboard/test_links.py
   :language: python
   :start-after: START test_message_with_inline_keyboard_example
   :end-before: END test_message_with_inline_keyboard_example


.. _message_with_reply_keyboard_example:
Клавиатура (Внизу чата)
-----------------------

.. literalinclude:: ../../demo/examples/keyboard/examples.py
   :language: python
   :start-after: START message_with_reply_keyboard_example
   :end-before: END message_with_reply_keyboard_example

Пример теста
~~~~~~~~~~~~

.. literalinclude:: ../../demo/tests/test_examples/test_keyboard/test_links.py
   :language: python
   :start-after: START test_message_with_reply_keyboard_example
   :end-before: END test_message_with_reply_keyboard_example
