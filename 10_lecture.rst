10. HTTP, requests
==================

Hashing
-------

- hash function
- hash()

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

HTTP
----

Python HTTP server
~~~~~~~~~~~~~~~~~~

Run a server::

  python -m http.server

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

Scrapy
------

Phg
---

- https://github.com/hvnsweeting/phg
- https://pypi.python.org/pypi/phg

Distributing module
-------------------

- https://docs.python.org/2/distutils/introduction.html
- https://docs.python.org/2/install/index.html
