Lecture 05
=========
Create and del object
---------------------

del xyz

IO
--

Handling Input and Output.

Read & write file
-----------------

Introduce using file.
open(), modes, close(), with, iter over lines.

Iterate over lines::

  with open('/etc/hosts') as f:
      for line in f:
          print(line, end='')
  print("Has file f closed? {0}".format(f.closed))

Module
------

- import modulename
- from module import name, namespace pollution
- __init__.py

pep8
----

Function
--------

- Built-in functions
- User-defined function
- Function name, indent
- Return None, return value
- Keyword argument, position argument
- Default argument, position, default value types
- Local variable scope
- Return best practice (one type only)
- When to write a function (need to repeat more than twice)
- Mandatory arguments, optional arguments
- Positional arguments, keyword arguments
- Side effect
- Function in function
- Meaning of function which has name starts with ``_``
- ``*args, **kwargs, print(*args)``  # after dict only
- Recursive function

Global variable
---------------

- Create, access, modify, import
- Compare to local variable
- Global is evil


::

    v = range(1, 10, 2)
    # python 3 range returns <range>(generator) instead of list, similar to xrange in python 2

::

    print(list(v))

::

    [1, 3, 5, 7, 9]

list comprehension
------------

::

    # let's do list comprehension

    squares = [x**2 for x in v]
    squares

::

    [1, 9, 25, 49, 81]

::

    # list comprehension with condition (optional)
    [x**2 for x in v if x%3 == 0]

::

    [9, 81]

.. figure:: http://python-3-patterns-idioms-test.readthedocs.org/en/latest/_images/listComprehensions.gif
   :align: center
   :alt:

inside the brackets ``[ ]`` is called a *generator expression*
----------------------

iterable - iterator - generator:
--------------------------------

.. figure:: http://nvie.com/img/relationships.png
   :align: center
   :alt:

According to the `python
documentation <https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions>`_,
**a list comprehension consists of square brackets containing an
expression followed by a for clause and zero or more for or if clauses
as shown below:**

::

    [expression for item1 in iterable1 if condition1
                for item2 in iterable2 if condition2
                ...
                for itemN in iterableN if conditionN ]

.. figure:: http://thelivingpearl.com/files/2013/01/wpid-450px-International_Morse_Code.svg-2013-01-8-08-28.png
   :align: center
   :alt:

.. figure:: http://thelivingpearl.com/files/2013/01/wpid-SOS_morse_code-2013-01-8-08-28.png
   :align: center
   :alt:

::

    MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
                'D': '-..',    'E': '.',      'F': '..-.',
                'G': '--.',    'H': '....',   'I': '..',
                'J': '.---',   'K': '-.-',    'L': '.-..',
                'M': '--',     'N': '-.',     'O': '---',
                'P': '.--.',   'Q': '--.-',   'R': '.-.',
                 'S': '...',    'T': '-',      'U': '..-',
                'V': '...-',   'W': '.--',    'X': '-..-',
                'Y': '-.--',   'Z': '--..',
                '0': '-----',  '1': '.----',  '2': '..---',
                '3': '...--',  '4': '....-',  '5': '.....',
                '6': '-....',  '7': '--...',  '8': '---..',
                '9': '----.'
            }

    # copy from here: http://bit.ly/pyfml_morse

::

    s1 = 'SOS'
    print(s1, '    '.join([MORSE_CODE[c.upper()] for c in s1]))

::

    SOS ...    ---    ...

::

    # translate your name to morse code
    s1 = 'hoang thanh long'
    print(s1, '    '.join([MORSE_CODE[c.upper()] for c in s1]))

::

    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-7-7ba35da7836f> in <module>()
          1 # translate your name to morse code
          2 s1 = 'hoang thanh long'
    ----> 3 print(s1, '    '.join([MORSE_CODE[c.upper()] for c in s1]))


    <ipython-input-7-7ba35da7836f> in <listcomp>(.0)
          1 # translate your name to morse code
          2 s1 = 'hoang thanh long'
    ----> 3 print(s1, '    '.join([MORSE_CODE[c.upper()] for c in s1]))


    KeyError: ' '

::

    # translate your name to morse code
    s1 = 'hoang thanh long'
    # only translate characters in MORSE_CODE
    print(s1, '    '.join([MORSE_CODE[c.upper()] for c in s1 if c.upper() in MORSE_CODE]))

::

    hoang thanh long ....    ---    .-    -.    --.    -    ....    .-    -.    ....    .-..    ---    -.    --.

*Want to convert from morse code to alphabet?*
----------------------------------------------

    There's a silence lasting exactly as long as a dot, between letters.
    And, between words, a pause that lasts exactly as long as seven
    dots.

    Obviously that's when the transmission obeys the standard rules.
    Otherwise, each transmissionist (is that even a word these days?)
    can wait however long he likes.

https://www.quora.com/How-do-you-separate-letters-in-Morse-code-How-do-you-separate-words

Homework:
-----------

1. write a function that translate alphabet to morse code (translate
   space to a custom separator)
2. write a function that translate morse code to alphabet with a
   parameter as separator for spaces before translating, remove all
   special characters, except a-z, 0-9 and spaces.

--------------

VN geography
------------

::

    provinces = [
                {'name':'An Giang','population':2153700,'area':3536.7,'senator':10},
                {'name':'Bà Rịa - Vũng Tàu','population':1039200,'area':1989.5,'senator':6},
                {'name':'Bạc Liêu','population':873400,'area':2468.7,'senator':6},
                {'name':'Bắc Kạn','population':301000,'area':4859.4,'senator':6},
                {'name':'Bắc Giang','population':1588500,'area':3848.9,'senator':8},
                {'name':'Bắc Ninh','population':1079900,'area':822.7,'senator':6},
                {'name':'Bến Tre','population':1258500,'area':2357.7,'senator':7},
                {'name':'Bình Dương','population':1748000,'area':2694.4,'senator':8},
                {'name':'Bình Định','population':1501800,'area':6050.6,'senator':8},
                {'name':'Bình Phước','population':912700,'area':6871.5,'senator':6},
                {'name':'Bình Thuận','population':1193500,'area':7812.8,'senator':7},
                {'name':'Cà Mau','population':1217100,'area':5294.9,'senator':7},
                {'name':'Cao Bằng','population':515200,'area':6707.9,'senator':6},
                {'name':'Cần Thơ','population':1214100,'area':1409,'senator':7},
                {'name':'Đà Nẵng','population':973800,'area':1285.4,'senator':6},
                {'name':'Đắk Lắk','population':1796700,'area':13125.4,'senator':9},
                {'name':'Đắk Nông','population':543200,'area':6515.6,'senator':6},
                {'name':'Đồng Nai','population':2720800,'area':5907.2,'senator':11},
                {'name':'Đồng Tháp','population':1676300,'area':3377,'senator':8},
                {'name':'Điện Biên','population':519300,'area':9562.9,'senator':6},
                {'name':'Gia Lai','population':1342700,'area':15536.9,'senator':7},
                {'name':'Hà Giang','population':758000,'area':7914.9,'senator':6},
                {'name':'Hà Nam','population':790000,'area':860.5,'senator':6},
                {'name':'Hà Nội','population':6844100,'area':3323.6,'senator':30},
                {'name':'Hà Tĩnh','population':1230500,'area':5997.8,'senator':7},
                {'name':'Hải Dương','population':1735100,'area':1656,'senator':9},
                {'name':'Hải Phòng','population':1904100,'area':1523.9,'senator':9},
                {'name':'Hòa Bình','population':806100,'area':4608.7,'senator':6},
                {'name':'Hậu Giang','population':769700,'area':1602.5,'senator':6},
                {'name':'Hưng Yên','population':1145600,'area':926,'senator':7},
                {'name':'TP. Hồ Chí Minh','population':7681700,'area':2095.6,'senator':30},
                {'name':'Khánh Hòa','population':1183000,'area':5217.7,'senator':7},
                {'name':'Kiên Giang','population':1726200,'area':6348.5,'senator':9},
                {'name':'Kon Tum','population':462400,'area':9689.6,'senator':6},
                {'name':'Lai Châu','population':397500,'area':9068.8,'senator':6},
                {'name':'Lào Cai','population':646800,'area':6383.9,'senator':6},
                {'name':'Lạng Sơn','population':744100,'area':8320.8,'senator':6},
                {'name':'Lâm Đồng','population':1234600,'area':9773.5,'senator':7},
                {'name':'Long An','population':1458200,'area':4492.4,'senator':8},
                {'name':'Nam Định','population':1836900,'area':1652.6,'senator':9},
                {'name':'Nghệ An','population':2952000,'area':16490.9,'senator':13},
                {'name':'Ninh Bình','population':915900,'area':1376.7,'senator':6},
                {'name':'Ninh Thuận','population':576700,'area':3358.3,'senator':6},
                {'name':'Phú Thọ','population':1335900,'area':3533.4,'senator':7},
                {'name':'Phú Yên','population':877200,'area':5060.6,'senator':6},
                {'name':'Quảng Bình','population':857900,'area':8065.3,'senator':6},
                {'name':'Quảng Nam','population':1450100,'area':10438.4,'senator':8},
                {'name':'Quảng Ngãi','population':1227900,'area':5153,'senator':7},
                {'name':'Quảng Ninh','population':1177200,'area':6102.3,'senator':7},
                {'name':'Quảng Trị','population':608100,'area':4739.8,'senator':6},
                {'name':'Sóc Trăng','population':1301900,'area':3311.6,'senator':7},
                {'name':'Sơn La','population':1134300,'area':14174.4,'senator':7},
                {'name':'Tây Ninh','population':1089900,'area':4039.7,'senator':6},
                {'name':'Thái Bình','population':1868800,'area':1570,'senator':9},
                {'name':'Thái Nguyên','population':1150200,'area':3534.7,'senator':7},
                {'name':'Thanh Hóa','population':3426600,'area':11132.2,'senator':16},
                {'name':'Thừa Thiên - Huế','population':1114500,'area':5033.2,'senator':7},
                {'name':'Tiền Giang','population':1692500,'area':2508.3,'senator':8},
                {'name':'Trà Vinh','population':1015300,'area':2341.2,'senator':6},
                {'name':'Tuyên Quang','population':738900,'area':5867.3,'senator':5},
                {'name':'Vĩnh Long','population':1033600,'area':1504.9,'senator':6},
                {'name':'Vĩnh Phúc','population':1020600,'area':1236.5,'senator':6},
                {'name':'Yên Bái','population':764400,'area':6886.3,'senator':7}
    ]

    # https://vi.wikipedia.org/wiki/T%E1%BB%89nh_th%C3%A0nh_Vi%E1%BB%87t_Nam#Danh_s.C3.A1ch_c.C3.A1c_t.E1.BB.89nh
    # copy from here: http://bit.ly/pyfml_vn_provinces

::

    print(['{[name]}: {[population]}'.format(p, p) for p in provinces if p['name'].startswith('H')])

::

    ['Hà Giang: 758000', 'Hà Nam: 790000', 'Hà Nội: 6844100', 'Hà Tĩnh: 1230500', 'Hải Dương: 1735100', 'Hải Phòng: 1904100', 'Hòa Bình: 806100', 'Hậu Giang: 769700', 'Hưng Yên: 1145600']

::

    # provinces with more than a million people
    more_than_a_million = [(p['name'], p['population']) for p in provinces if p['population'] > 10**6]
    print(more_than_a_million)

::

    [('An Giang', 2153700), ('Bà Rịa - Vũng Tàu', 1039200), ('Bắc Giang', 1588500), ('Bắc Ninh', 1079900), ('Bến Tre', 1258500), ('Bình Dương', 1748000), ('Bình Định', 1501800), ('Bình Thuận', 1193500), ('Cà Mau', 1217100), ('Cần Thơ', 1214100), ('Đắk Lắk', 1796700), ('Đồng Nai', 2720800), ('Đồng Tháp', 1676300), ('Gia Lai', 1342700), ('Hà Nội', 6844100), ('Hà Tĩnh', 1230500), ('Hải Dương', 1735100), ('Hải Phòng', 1904100), ('Hưng Yên', 1145600), ('TP. Hồ Chí Minh', 7681700), ('Khánh Hòa', 1183000), ('Kiên Giang', 1726200), ('Lâm Đồng', 1234600), ('Long An', 1458200), ('Nam Định', 1836900), ('Nghệ An', 2952000), ('Phú Thọ', 1335900), ('Quảng Nam', 1450100), ('Quảng Ngãi', 1227900), ('Quảng Ninh', 1177200), ('Sóc Trăng', 1301900), ('Sơn La', 1134300), ('Tây Ninh', 1089900), ('Thái Bình', 1868800), ('Thái Nguyên', 1150200), ('Thanh Hóa', 3426600), ('Thừa Thiên - Huế', 1114500), ('Tiền Giang', 1692500), ('Trà Vinh', 1015300), ('Vĩnh Long', 1033600), ('Vĩnh Phúc', 1020600)]

Something not geographic here, let's remove them
------------------------------------------------

::

    import pprint

::

    provinces = [{'name': d['name'], 'population': d['population'], 'area': d['area']} for d in provinces]
    pprint.pprint(provinces)
    # no senator left

::

    [{'area': 3536.7, 'name': 'An Giang', 'population': 2153700},
     {'area': 1989.5, 'name': 'Bà Rịa - Vũng Tàu', 'population': 1039200},
     {'area': 2468.7, 'name': 'Bạc Liêu', 'population': 873400},
     {'area': 4859.4, 'name': 'Bắc Kạn', 'population': 301000},
     {'area': 3848.9, 'name': 'Bắc Giang', 'population': 1588500},
     {'area': 822.7, 'name': 'Bắc Ninh', 'population': 1079900},
     {'area': 2357.7, 'name': 'Bến Tre', 'population': 1258500},
     {'area': 2694.4, 'name': 'Bình Dương', 'population': 1748000},
     {'area': 6050.6, 'name': 'Bình Định', 'population': 1501800},
     {'area': 6871.5, 'name': 'Bình Phước', 'population': 912700},
     {'area': 7812.8, 'name': 'Bình Thuận', 'population': 1193500},
     {'area': 5294.9, 'name': 'Cà Mau', 'population': 1217100},
     {'area': 6707.9, 'name': 'Cao Bằng', 'population': 515200},
     {'area': 1409, 'name': 'Cần Thơ', 'population': 1214100},
     {'area': 1285.4, 'name': 'Đà Nẵng', 'population': 973800},
     {'area': 13125.4, 'name': 'Đắk Lắk', 'population': 1796700},
     {'area': 6515.6, 'name': 'Đắk Nông', 'population': 543200},
     {'area': 5907.2, 'name': 'Đồng Nai', 'population': 2720800},
     {'area': 3377, 'name': 'Đồng Tháp', 'population': 1676300},
     {'area': 9562.9, 'name': 'Điện Biên', 'population': 519300},
     {'area': 15536.9, 'name': 'Gia Lai', 'population': 1342700},
     {'area': 7914.9, 'name': 'Hà Giang', 'population': 758000},
     {'area': 860.5, 'name': 'Hà Nam', 'population': 790000},
     {'area': 3323.6, 'name': 'Hà Nội', 'population': 6844100},
     {'area': 5997.8, 'name': 'Hà Tĩnh', 'population': 1230500},
     {'area': 1656, 'name': 'Hải Dương', 'population': 1735100},
     {'area': 1523.9, 'name': 'Hải Phòng', 'population': 1904100},
     {'area': 4608.7, 'name': 'Hòa Bình', 'population': 806100},
     {'area': 1602.5, 'name': 'Hậu Giang', 'population': 769700},
     {'area': 926, 'name': 'Hưng Yên', 'population': 1145600},
     {'area': 2095.6, 'name': 'TP. Hồ Chí Minh', 'population': 7681700},
     {'area': 5217.7, 'name': 'Khánh Hòa', 'population': 1183000},
     {'area': 6348.5, 'name': 'Kiên Giang', 'population': 1726200},
     {'area': 9689.6, 'name': 'Kon Tum', 'population': 462400},
     {'area': 9068.8, 'name': 'Lai Châu', 'population': 397500},
     {'area': 6383.9, 'name': 'Lào Cai', 'population': 646800},
     {'area': 8320.8, 'name': 'Lạng Sơn', 'population': 744100},
     {'area': 9773.5, 'name': 'Lâm Đồng', 'population': 1234600},
     {'area': 4492.4, 'name': 'Long An', 'population': 1458200},
     {'area': 1652.6, 'name': 'Nam Định', 'population': 1836900},
     {'area': 16490.9, 'name': 'Nghệ An', 'population': 2952000},
     {'area': 1376.7, 'name': 'Ninh Bình', 'population': 915900},
     {'area': 3358.3, 'name': 'Ninh Thuận', 'population': 576700},
     {'area': 3533.4, 'name': 'Phú Thọ', 'population': 1335900},
     {'area': 5060.6, 'name': 'Phú Yên', 'population': 877200},
     {'area': 8065.3, 'name': 'Quảng Bình', 'population': 857900},
     {'area': 10438.4, 'name': 'Quảng Nam', 'population': 1450100},
     {'area': 5153, 'name': 'Quảng Ngãi', 'population': 1227900},
     {'area': 6102.3, 'name': 'Quảng Ninh', 'population': 1177200},
     {'area': 4739.8, 'name': 'Quảng Trị', 'population': 608100},
     {'area': 3311.6, 'name': 'Sóc Trăng', 'population': 1301900},
     {'area': 14174.4, 'name': 'Sơn La', 'population': 1134300},
     {'area': 4039.7, 'name': 'Tây Ninh', 'population': 1089900},
     {'area': 1570, 'name': 'Thái Bình', 'population': 1868800},
     {'area': 3534.7, 'name': 'Thái Nguyên', 'population': 1150200},
     {'area': 11132.2, 'name': 'Thanh Hóa', 'population': 3426600},
     {'area': 5033.2, 'name': 'Thừa Thiên - Huế', 'population': 1114500},
     {'area': 2508.3, 'name': 'Tiền Giang', 'population': 1692500},
     {'area': 2341.2, 'name': 'Trà Vinh', 'population': 1015300},
     {'area': 5867.3, 'name': 'Tuyên Quang', 'population': 738900},
     {'area': 1504.9, 'name': 'Vĩnh Long', 'population': 1033600},
     {'area': 1236.5, 'name': 'Vĩnh Phúc', 'population': 1020600},
     {'area': 6886.3, 'name': 'Yên Bái', 'population': 764400}]

::

    students = [
        {'name': 'Dai', 'literature': 5, 'history': 7, 'geography': 5},
        {'name': 'Hung', 'literature': 7, 'history': 8, 'geography': 6},
        {'name': 'Long', 'literature': 1.5, 'history': 5, 'geography': 8}
    ]

    average = [{'name': m['name'], 'average': '{:.2f}'.format((m['literature'] + m['history'] + m['geography'])/3)}
               for m in students]
    print(average)

::

    [{'name': 'Dai', 'average': '5.67'}, {'name': 'Hung', 'average': '7.00'}, {'name': 'Long', 'average': '4.83'}]

::

    rank = [(student['name'], 'Good' if float(student['average']) > 5.0 else 'Bad') for student in average]
    print(rank)

::

    [('Dai', 'Good'), ('Hung', 'Good'), ('Long', 'Bad')]

