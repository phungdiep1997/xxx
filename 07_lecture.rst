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


Module
------

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

Duck typing
~~~~~~~~~~~

Monkey Patch
------------
