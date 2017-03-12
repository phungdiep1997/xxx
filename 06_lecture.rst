6. File, JSON, Function, Module, Lint
=====================================

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

JSON
----

CSV
---

Pickle
------

User-defined function
---------------------

double = lambda x: x * 2
print(double(2))

sum2 = lambda x, y: x + y

Function
--------

- Built-in functions
- User-defined function::

    def func_name(arg1, args):  # function signature
        '''Docstring
        end of docstring'''

        body_of_function
        return something

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

::
    def calculate_average_age(first_age, second_age):
        total_of_all_ages = first_age + second_age
        return total_of_all_ages / 2

Module
------

- import modulename
- from module import name, namespace pollution
- __init__.py

Global variable
---------------

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
