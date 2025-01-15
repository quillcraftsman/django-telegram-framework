Developer Documentation
-----------------------

Install requirement
^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    pip install -r requirements.txt
    pip install -r dev-requirements.txt
    pip install -r doc-requirements.txt

Makefile
^^^^^^^^

First check **Makefile**. It contains many useful commands to work with the project:

.. include:: ../Makefile

Get started
^^^^^^^^^^^

You can start with test and test coverage:

.. code-block:: shell

    make coverage
    make test

Check lint and test coverage before sending pull-request

.. code-block:: shell

    make lint

Build documentation
^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    make package_docs
    cd docs
    make clean html
    make html
