Lecture 08
==========

decorator
---------

- functions are object.
- function is callable.
- function which returns other function
- use @ notation
- just syntactic sugar
- check all syntactic sugars: ``+``, ``-``, ``__getitem__``,
  ``__str__``.

Stdlib
---------

GitLab issues
-------------

https://gitlab.com/hvn_familug/pyfml1604/issues

script
------

- a text file (python module) that can run
- chmod::

    ls -l scriptname.py
    chmod a+x scriptname.py
    ls -l scriptname.py

- #!/usr/bin/env python3
- https://docs.python.org/3/faq/library.html#how-do-i-make-a-python-script-executable-on-unix

lambda
------

- https://docs.python.org/3/glossary.html#term-lambda
- map, filter

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

- sys.exit
- sys.argv

pdb
---

The python debugger https://docs.python.org/3/library/pdb.html ::

  python3 -m pdb myscript.py

timeit
------

Use with ipython %timeit::

  In [2]: %timeit 'x = range(1000,1); sorted(x)'
  The slowest run took 381.51 times longer than the fastest. This could mean that an intermediate result is being cached
  100000000 loops, best of 3: 13.1 ns per loop

http server - python 3 version
----------------

Run a server::

  python -m http.server

json
----

- often used for API
- Dump json::

  $ echo '{"message": "Validation Failed", "errors": [{"field": "title", "code": "missing_field", "resource": "Issue"}]}' | python -m json.tool
  {
      "errors": [
          {
              "code": "missing_field",
              "field": "title",
              "resource": "Issue"
          }
      ],
      "message": "Validation Failed"
  }

TDD
---

- unittest
- BDD
- http://flask.pocoo.org/docs/0.10/testing/
- https://docs.djangoproject.com/en/1.8/topics/testing/

yaml
----

- http://www.familug.org/2013/06/yaml-la-gi.html
- often used for config files
- pip install pyyaml, import yaml, yaml.dump, yaml.load

algorithm time complexity
-------------------------

- Comparing O(N), O(N^2), O(lg(N)), O(N!)
