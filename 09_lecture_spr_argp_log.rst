Lecture 09
==========

Reading code is more important that write
-----------------------------------------

https://github.com/saltstack/salt/blob/develop/salt/utils/__init__.py

Function aliasing
-----------------

https://github.com/saltstack/salt/blob/develop/salt/states/virtualenv_mod.py#L274

random
------

https://docs.python.org/2/faq/library.html#mathematics-and-numerics

time
----

- sleep()
- time()
- while True / time.sleep best practice

datetime
--------

- calculate timedelta
- format and parse time object

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

logging
-------

- basicConfig
- getLogger(__name__)
- debug/info/warning/error/critical
- do not format log, let logger does that.

collections
-----------

- namedtuple
- Counter
- defaultdict
- deque
- OrderedDict

generator
---------

- https://docs.python.org/3/glossary.html#term-generator
- Return generator expression::

    return (s for s in students)

iterator
--------

- how ``for`` works: https://docs.python.org/3/tutorial/classes.html#iterators
- what is iterate?
- Convert to a list?
- list??

special methods
---------------

- callable object: __call__
- accessing value by using index: __getitem__

itertools
---------

functools
---------

PYMOTW
------

https://pymotw.com/3/py-modindex.html
