5. Import, Set, Dict
====================

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
