7. Exception, Package, class
============================

Exception
---------

- try/except/else syntax
- except vs except Exception
- multiple except clauses vs using tuple
- why they know what to except
- also a control flow

LBYL
----

https://docs.python.org/2/glossary.html#term-lbyl

Namespace & global variable
---------------------------

- Each module is a namespace
- Create, access, modify, import
- Compare to local variable
- Global is evil

Generator
---------

- https://docs.python.org/3/glossary.html#term-generator
- Return generator expression::

    return (s for s in students)

Iterator
--------

- how ``for`` works: https://docs.python.org/3/tutorial/classes.html#iterators
- what is iterate?
- Convert to a list?
- list??

Module
------

- import modulename
- from module import name, namespace pollution
- __init__.py
- Example: each create a package, and a module, and import function from it::

  mkdir my_name; touch my_name/{__init__,utils}.py
  import my_name
  import my_name.utils as mutils
  mutils.func_name(xyz)
  import this #  why import twice but print once?

- how import works? - how it choose what to import?

Class
-----

- Class is a way to represent data (compare to python builtin-data type).
- Class is a way to organize code (compare to module).
- Singleton design pattern.
- Inheritance and example with a software which needs multiple output
  (HTML, PDF, Text).

Linting
-------

What does ``lint`` mean? -> https://en.wikipedia.org/wiki/Lint\_(software)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    tool that flags suspicious usage in software written in any computer
    language

PyLint:
-------

Install pylint: https://www.pylint.org/#install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``sudo apt-get install pylint``

or ``pip install pylint``

usage: `read the docs <https://docs.pylint.org/>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

basic usage: ``pylint /path/to/mymodule.py``


Duck typing
~~~~~~~~~~~

Monkey Patch
------------
