Preparing
---------

- install pip and virtualenv (see tutorial below)

with statement
--------------

- auto close resources.
- context manager protocol.
  https://docs.python.org/2/whatsnew/2.6.html?highlight=contextmanager#pep-343-the-with-statement

introspection
-------------

- https://en.wikipedia.org/wiki/Type_introspection
- ``dir``
- import inspect
- how IDE of static typing language know wrong type function call without
  running the code, but Python cannot?::

    def love_me(yes):
        return yes

    yes = argv[1]
    if love_me(yes):
        print 'xong leeeeeeeen'
    else:
        print 'tra dep bo ve'

Pip
---

- https://pip.pypa.io/en/stable/
- http://pypi.python.org/

Install
~~~~~~~

On Ubuntu::

  sudo apt-get install -y python-pip

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

Virtualenv
----------

Install
~~~~~~~

On ubuntu 12.04::

  sudo apt-get install -y python-virtualenv

Using
~~~~~

Create new virtualenv::

  virtualenv venv_name

Use environment ``venv_name``::

  source venv_name/bin/activate

Stop using::

  deactivate

Install package inside virtualenv::

  pip install ipython requests mpho six

Be social
---------

- Register an account on `LinkedIn <https://www.linkedin.com/>`_
- Register an account on `GitHub <https://github.com/>`_ and create 1 repo.

Requests
--------

- import requests; request??
- http://docs.python-requests.org/en/latest/user/quickstart/
- HTTP, client-server
- HTTP client, FireFox web console: https://developer.mozilla.org/en/docs/Tools/Web_Console
- HTTP methods: http://flask.pocoo.org/docs/0.10/quickstart/#http-methods

BeautifulSoup4
--------------

- parsing HTML
- http://www.crummy.com/software/BeautifulSoup/bs4/doc/

Pho
---

- https://github.com/hvnsweeting/pho

Distributing module
-------------------

- https://docs.python.org/2/distutils/introduction.html
- https://docs.python.org/2/install/index.html
