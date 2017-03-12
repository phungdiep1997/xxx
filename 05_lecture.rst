Lecture 06
=========

Iterable
--------

Iterator
--------

- how ``for`` works: https://docs.python.org/3/tutorial/classes.html#iterators
- what is iterate?
- Convert to a list?
- list??

Generator
---------

- https://docs.python.org/3/glossary.html#term-generator
- Return generator expression::

    return (s for s in students)

Reading code
------------

- Important than write
- Let's practice

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

Git
---

- git diff
- git show
- git log --graph
- workflow: checkout develop -> pull -> new_branch -> merge -> develop

Dictionary
----------

- Ways to create dict: literal, dict comprehension, dict(list of tuples)
- Only hashable objects can be used as key
- Present several real-world dicts
- Iterate over dict (k,v, items(), keys(), values())
- Iterate over key only
- Example with nested dict
- Dict keys has no order
- Introduction to JSON, serialization.
- Check membership (``x in list``)::

    if x in range(100000): # algorithm complexity O(N)
- Check membership of ``dict`` is ``O(1) - constant``

Function kwargs
---------------

- ``*args, **kwargs``

Pickle
------

JSON
----

YAML
----

Set
---

- Like list, but uniq items.
- Unordered, so there is no indexing
- Use set to ``-``
- Convert a list to a set
- dict.keys() are a set

Compare with is and ==
----------------------

- Use ``is`` only for boolean, ``None``, empty tuple.

Module
------

- import modulename
- from module import name, namespace pollution
- __init__.py

Misc
----

- continue, break in loop
- any, all
