3. GitLab, control flow, list
=============================

String methods
--------------

Format
------

- %s %d
- Hello {}".format(name)


Unicode
-------

str
---

and ``__str__``

List
----

- How to create an empty list?
- How to create a list with strings?
- How to create a list with numbers?
- Given::

    numbers = [1,2,3]

  How to have first item set to 5?
- How to check is ``7`` in above list (test membership)?
- How to check if 2 list are equals?
- What happen when plus (+) two lists?
- How to add an element to a list?
- We can indexing and slice list like with string, how
  to reverse a list? It returns WHAT?
- 9 methods, built-in function ``reversed``, ``sorted``
  Each method RETURN what?

Control flow
------------

- if/elif/else

Error handling
--------------

try/except
Having a list of 12 months, how to handle if user enter wrong input?

Loops and iteration
-------------------

- for ... in
- while
- continue, break

Bài tập: tưởng tượng bạn đang điều khiển con rắn săn mồi bằng các lệnh.
Viết code in ra màn hình "UP" (lên) 10 lần, rồi "RIGHT" (rẽ phải) 5 lần.

Bài tập 2: dùng while, in ra màn hình số integer tăng dần từ 1. Dừng lại nếu số nguyên đó chia cho 68 dư 1.

Introduce to git
----------------

Ternary
-------

Assign either value to a variable base on condition::

  x = 5
  is_even = True if x %2 == 0 else False
  print is_even

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

References
----------

- https://docs.python.org/3/tutorial/controlflow.html#more-control-flow-tools
- https://docs.python.org/3/library/stdtypes.html#str.format