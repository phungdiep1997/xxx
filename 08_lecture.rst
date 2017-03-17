8. stdlib, decorator, generator, debugging
==========================================

StackOverFlow
-------------

http://stackoverflow.com/questions/tagged/python

Glossary
--------

Generator
---------

- https://docs.python.org/3/glossary.html#term-generator
- Return generator expression::

    return (s for s in students)

decorator
---------

- functions are object.
- function is callable.
- function which returns other function
- use @ notation
- just syntactic sugar
- check all syntactic sugars: ``+``, ``-``, ``__getitem__``,
  ``__str__``.

script
------

- a text file (python module) that can run
- chmod::

    ls -l scriptname.py
    chmod a+x scriptname.py
    ls -l scriptname.py

- #!/usr/bin/env python3
- https://docs.python.org/3/faq/library.html#how-do-i-make-a-python-script-executable-on-unix

Stdlib
------

PYMOTW
------

https://docs.python.org/3/library/
https://docs.python.org/3/howto/
https://pymotw.com/3/py-modindex.html

time
----

- sleep()
- time()
- while True / time.sleep best practice

pdb
---

The python debugger https://docs.python.org/3/library/pdb.html ::

  python3 -m pdb myscript.py


- When script *doesn't run*, what to do?
- ``python -m pdb /path/script.py -t option``


random
------

https://docs.python.org/2/faq/library.html#mathematics-and-numerics

datetime
--------

- calculate timedelta
- format and parse time object

timeit
------

Use with ipython %timeit::

  In [2]: %timeit 'x = range(1000,1); sorted(x)'
  The slowest run took 381.51 times longer than the fastest. This could mean that an intermediate result is being cached
  100000000 loops, best of 3: 13.1 ns per loop

collections
-----------

- namedtuple
- Counter
- defaultdict
- deque
- OrderedDict

logging
-------

- basicConfig
- getLogger(__name__)
- debug/info/warning/error/critical
- do not format log, let logger does that.

copy
----

- Assignment statements do not copy objects.
  They create binding between a target and an object.
- Interface of a module is function signatures, exceptions (all thing exposed).
- Shallow vs deep copy, how does they implemented?
- What are copy methods for list and dict, shallow or deep?
- https://docs.python.org/3/library/copy.html
- E.g: when to not use deep copy
  https://github.com/saltstack/salt/commit/63aa8c686bcb0ebc47eb3fc80ac45001e92320ff

os
--

- os.listdir
- os.getuid
- os.getpid
- os.walk
- os.path.join
- os.path.abspath
- os.path.isfile
- os.path.isdir
- os.path.exists

sys
---

- sys.path
- sys.exit
- sys.argv

yaml
----

- http://www.familug.org/2013/06/yaml-la-gi.html
- often used for config files
- pip install pyyaml, import yaml, yaml.dump, yaml.load

Duck typing
~~~~~~~~~~~

Monkey Patch
------------

algorithm time complexity
-------------------------

- Comparing O(N), O(N^2), O(lg(N)), O(N!)

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
