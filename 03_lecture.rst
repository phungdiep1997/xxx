Lecture 03
==========

Introduce to git
----------------

- Create gitlab.com account
- TODO at home: install git

Membership test
---------------

``in``

Boolean
-------

- and/or/not
- short-circuit (``True and False and 1/0``)

Control flow
------------

- if/elif/else
- for ... in
- while
- continue, break

Exception
---------

- try/except/else syntax
- except vs except Exception
- multiple except clauses vs using tuple
- why they know what to except

Ternary
-------

Assign either value to a variable base on condition::

  x = 5
  is_even = True if x %2 == 0 else False
  print is_even

List
----

- Create empty list
- Assign element
- Compare
- Plus (+)
- Check membership (``x in list``)::

    if x in range(100000): # algorithm complexity O(N)

- Check membership of ``dict`` is ``O(1) - constant``
- 9 methods, built-in function ``reversed``, ``sorted``
- Reverse with ``li[::-1]``
- list comprehension (map/filter), only when need a list

Built-in Functions
------------------

- len
- id
- dir
- sum
- str
- int
- bool

Methods
-------

- all
- check membership
- len

Format
------

- %
- format()

Unicode
-------

str
---

and ``__str__``
