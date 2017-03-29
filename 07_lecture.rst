7. Exception, Package, Virtualenv, Pip, Class
=============================================

Exception
---------

- try/except/else syntax
- except vs except Exception
- multiple except clauses vs using tuple
- why they know what to except
- also a control flow

LBYL vs EAFP
------------

https://docs.python.org/3/glossary.html#term-lbyl
https://docs.python.org/3/glossary.html#term-eafp

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

Namespace & global variable
---------------------------

- Each module is a namespace
- Create, access, modify, import
- Compare to local variable
- Global is evil

Virtualenv
----------

https://docs.python.org/3/tutorial/venv.html

For modifying sys.path of program run inside virtualenv.
Each virtualenv is just a directory, when using pip, you install
packages to that directory.

Install
~~~~~~~

::

  sudo pip install virtualenv # sudo on OSX, Linux


Using
~~~~~

Create new virtualenv::

  virtualenv -p python3 pymi

Use environment ``pymi``::

  source pymi/bin/activate

Stop using::

  deactivate

Install package inside virtualenv::

  pip install -r requirements.txt

Pip
---

- https://pip.pypa.io/en/stable/
- http://pypi.python.org/

Command
~~~~~~~

- Install a package::

  $ pip install package_name

- Uninstall a package::

  $ pip uninstall package_name

- List all installed packages::

  $ pip freeze
  $ pip freeze > requirements.txt

- Install all requirements from requirements.txt::

  $ pip install -r requirements.txt

- Search package::

  $ pip search pkg_name

- Options:

  ``-v`` ``-d``

- Pip install packages from github:

  $ pip install git+git://github.com/myuser/foo.git@v123

Iterator
--------

- how ``for`` works: https://docs.python.org/3/tutorial/classes.html#iterators
  Behind the scenes, the for statement calls iter() on the container object. The function returns an iterator object that defines the method __next__() which accesses elements in the container one at a time. When there are no more elements, __next__() raises a StopIteration exception which tells the for loop to terminate.
- what is iterate?
- convert list to iterator
- iter()
- next()

Class
-----

- We already used class::

  In [4]: import inspect

  In [5]: [inspect.isclass(i) for i in (int, float, str, list, dict, set, bool)]
  Out[5]: [True, True, True, True, True, True, True]

- Create new integer object by int(6)
- Create new dict object by dict::

  In [9]: dict(name='Python', birth=1991)
  Out[9]: {'birth': 1991, 'name': 'Python'}

- Define MyDict that mimic above dict.
- Class is a way to represent data.
- Class is a way to organize code (compare to module).
- __init__, __str__
- Single inheritance.

Exception hierarchy
-------------------

exceptions are classes.

https://docs.python.org/3/library/exceptions.html#exception-hierarchy
