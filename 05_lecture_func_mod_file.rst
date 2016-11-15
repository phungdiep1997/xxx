Lecture 05
=========
Create and del object
---------------------

del xyz

IO
--

Handling Input and Output.

Read & write file
-----------------

Introduce using file.
open(), modes, close(), with, iter over lines.

Iterate over lines::

  with open('/etc/hosts') as f:
      for line in f:
          print(line, end='')
  print("Has file f closed? {0}".format(f.closed))

Module
------

- import modulename
- from module import name, namespace pollution
- __init__.py

pep8
----

Function
--------

- Built-in functions
- User-defined function
- Function name, indent
- Return None, return value
- Keyword argument, position argument
- Default argument, position, default value types
- Local variable scope
- Return best practice (one type only)
- When to write a function (need to repeat more than twice)
- Mandatory arguments, optional arguments
- Positional arguments, keyword arguments
- Side effect
- Function in function
- Meaning of function which has name starts with ``_``
- ``*args, **kwargs, print(*args)``  # after dict only
- Recursive function

Global variable
---------------

- Create, access, modify, import
- Compare to local variable
- Global is evil


::

    v = range(1, 10, 2)
    # python 3 range returns <range>(generator) instead of list, similar to xrange in python 2

::

    print(list(v))

::

    [1, 3, 5, 7, 9]

list comprehension
------------

::

    # let's do list comprehension

    squares = [x**2 for x in v]
    squares

::

    [1, 9, 25, 49, 81]

::

    # list comprehension with condition (optional)
    [x**2 for x in v if x%3 == 0]

::

    [9, 81]

.. figure:: http://python-3-patterns-idioms-test.readthedocs.org/en/latest/_images/listComprehensions.gif
   :align: center
   :alt:

inside the brackets ``[ ]`` is called a *generator expression*
----------------------

iterable - iterator - generator:
--------------------------------

.. figure:: http://nvie.com/img/relationships.png
   :align: center
   :alt:

According to the `python
documentation <https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions>`_,
**a list comprehension consists of square brackets containing an
expression followed by a for clause and zero or more for or if clauses
as shown below:**

::

    [expression for item1 in iterable1 if condition1
                for item2 in iterable2 if condition2
                ...
                for itemN in iterableN if conditionN ]