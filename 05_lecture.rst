5. Debug, Import, Set, Dict
===========================

Tuple unpacking
---------------

- Multi-assignment
- Unpacking in function call with `*`
- When list when tuple?

Debug
-----

- Run module with pdb
- Basic commands:

 > h: help
 > l: list
 > n: next
 > b: break
 > c: continue
 > p: print
 > s: step into

Import
------

- math
- import antigravity
- import this
- xkcd.com, news.ycombinator.com
- random

Python module
-------------

- What is a Python module?
- How to write a python module?
- How to run a Python module?

Set
---

- Like list, but uniq items.
- Unordered, so there is no indexing
- Use set to ``-``
- Convert a list to a set
- dict.keys() are a set

Compare with is and ==
----------------------

- Use ``is`` only for boolean, ``None``, empty tuple.

Dictionary
----------

- Ways to create dict: literal, dict comprehension, dict(list of tuples)
- Only hashable objects can be used as key
- Present several real-world dicts
- Iterate over dict (k,v, items(), keys(), values())
- Iterate over key only
- Example with nested dict
- Dict keys has no order
- Introduction to JSON, serialization.
- Check membership (``x in list``)::

    if x in range(100000): # algorithm complexity O(N)
- Check membership of ``dict`` is ``O(1) - constant``

Iterable
--------

List, tuple, dict, set, string.

Reading code
------------

- Important than write
- Let's practice https://github.com/saltstack/salt/blob/develop/salt/state.py

References
----------

- List vs Tuple

  http://docs.python.org/tutorial/datastructures.html#tuples-and-sequences
  http://docs.python3.org/faq/design.html#why-are-there-separate-tuple-and-list-data-types
  http://www.stackoverflow.com/questions/31192923/lists-vs-tuples-what-to-use-and-when
