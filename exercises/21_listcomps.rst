List comprehendsion
===================

21.1
----

Create a list which contain 10 elements ``2``.

21.2
----

Create a list which contains 10 random integer, which are >= 0, <= 9.

To generate 1 random integer, use::

  import random
  random.randint(0,9)

21.3
----

Create a list which contains 25 first even integers. ``[2, 4 ...]``

21.4
----

Create a string which contains 10 random ASCII letters.

To create 1 letter, use::

  import random
  import string
  random.choice(string.ascii_letters)

21.5
----

Create a list like this by listcomps::

  ['111111', '222222', ..., '999999']


21.6
----

Create a list contains all integer (not string) digit
of ten last digits of `2**1000`.

21.7
----

Create a list contains all integers less than 1001,
which are multiple of 3 or 5.

21.8
----

Create a list which contain n list, each list contains number from 1->10::

  [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

Then write code to print out two diagonals::

  0********0
  *1******1*
  **2****2**
  ***3**3***
  ****44****
  ****55****
  ***6**6***
  **7****7**
  *8******8*
  9********9
