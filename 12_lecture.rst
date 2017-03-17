12. System and Network
======================

Introspection
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


subprocess
----------

- The only/up-to-date way to run external commands (vs command/os.system)
- But using lib is better.
- import shlex

argparse
--------

- much better than sys.argv
- add_argument()
- parse_args()
- nargs
- optional vs position args
- store_true
- help
- default

itertools
---------

functools
---------

http server - python 3 version
-------------------------------

Run a server::

  python -m http.server

