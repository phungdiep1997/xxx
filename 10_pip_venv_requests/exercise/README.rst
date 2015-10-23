Exercise
========

10.1
----

Write a script to list all Github repositories of an user.

For example, user ``hvnsweeting``, use:
https://api.github.com/users/hvnsweeting/repos

Form::

  githubrepos.py username

Libs:

- argparse
- logging
- requests

10.2
----

Viết một script kiểm tra xem các số argument đầu vào có trúng lô không
(2 số cuối trùng với một giải nào đó). Nếu không có argument nào thì print
ra tất cả các giải từ đặc biệt -> giải 7.

Lấy kết quả từ ``ketqua.net``.

Form::

  ketqua.py [NUMBER1] [NUMBER2]

Libs:

- beautifulsoup4
- requests
- logging

Tips:

- ``nargs`` https://docs.python.org/2/library/argparse.html
