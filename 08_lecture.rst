8. virtualenv, pip, stdlib, decorator
=====================================

Virtualenv
----------

https://docs.python.org/3/tutorial/venv.html

Install
~~~~~~~

For python2 only.  On ubuntu 12.04::

  sudo apt-get install -y python-virtualenv

Python3 built-in already, no need to install.

Using
~~~~~

Create new virtualenv::

  python3 -m env

Use environment ``env``::

  source env/bin/activate

Stop using::

  deactivate

Install package inside virtualenv::

  pip install ipython requests pep8 ipdb six

Pip
---

- https://pip.pypa.io/en/stable/
- http://pypi.python.org/

Install
~~~~~~~

On Ubuntu::

  sudo apt-get install -y python3-pip

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

script
------

- a text file (python module) that can run
- chmod::

    ls -l scriptname.py
    chmod a+x scriptname.py
    ls -l scriptname.py

- #!/usr/bin/env python3
- https://docs.python.org/3/faq/library.html#how-do-i-make-a-python-script-executable-on-unix

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

yaml
----

- http://www.familug.org/2013/06/yaml-la-gi.html
- often used for config files
- pip install pyyaml, import yaml, yaml.dump, yaml.load

TDD
---

- unittest
- BDD
- http://flask.pocoo.org/docs/0.10/testing/
- https://docs.djangoproject.com/en/1.8/topics/testing/


algorithm time complexity
-------------------------

- Comparing O(N), O(N^2), O(lg(N)), O(N!)
