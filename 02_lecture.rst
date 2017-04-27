2. List, string, name
=====================

List
----

- Create list, append, pop

String
------

- Create string
- Single quote, double quote
- Triple quote
- Multi lines: ``triple quote, \\, ( ) ``
- Escaping ``\n \t \\ \' \"``
- What happen when we write s = "Python"   " Glory" ?
- We have s = "Python is great", I want to get only "Pet" from s,
  how to do that?
- We have s = "Python is great", I want to get only "Python", and only "great",
  how to do that?
- I have "Apple", I want "elppA", how to do it?
- How many characters are there in this string?
  s = "lỡ buông lời yêu em, sợ em xa lánh \
       biết sao giờ vì chỉ thấy nắng trong tim mình"
  How to not count them manually but use Python?
  ``len`` stands for ``length``
- What happen when I want to have "Jython" from s = "Python" if I try:
  s[0] = "J"
  What's wrong, why?
- Formatting
- ASCII, Unicode, bits and byte.
- HOMEWORK: write code that prints output when you copy and paste it on
  interpreter, it prints "Hello PyFML".

Variable
--------

Name
----

It's the hardest problem: http://pymi.vn/tutorial/naming/,
http://www.slideshare.net/pirhilton/how-to-name-things-the-hardest-problem-in-programming

Binding
~~~~~~~

Object
~~~~~~

name --binding--> object

.. image:: Resource/var_binding.jpg


- use id() to get "identify" of an object.
- two names bind to same object with have id(x) == id(y)


Deleting name
-------------

Before::

  ~Namespace~~~~\
  |name          \ --binding--> object
  |---------------

After::

  ~Namespace~~~~\
  |              \         object
  |---------------

And Garbage collector will collect object, remove it from memory.

Deletion of a name removes the binding of that name from the local or global
namespace, depending on whether the name occurs in a global statement in the
same code block. If the name is unbound, a NameError exception will be raised.

Builtin functions
-----------------

https://docs.python.org/3/library/functions.html

- help
- all
- any
- hex, int, str, octal type
- chr
- dir
- globals()
- locals
- input
- min
- max
- ord

Chuẩn bị trước buổi 3
---------------------

- Cài ipython bằng bất cứ cách nào có thể. Nếu trên máy có cài pip, gõ thử
  ``pip install ipython``  . Xem thêm tại http://ipython.org/install.html
- Cài đặt git lên máy (https://git-scm.com/downloads). Git là một công cụ
  có giao diện dòng lệnh (gõ các lệnh để làm việc). Nếu vì lý do gì mà không muốn
  gõ lệnh, hãy tự hỏi tại sao muốn gõ code? hoặc tải giao diện đồ hoạ ở đây
  https://git-scm.com/downloads/guis (SourceTree là ứng cử sáng giá).
- Học sử dụng git và gitlab: https://github.com/huyhoang17/Guide

References
----------

- https://docs.python.org/3/tutorial/introduction.html#lists
- https://docs.python.org/3/tutorial/introduction.html#strings
- https://pymi.vn/tutorial/string1/
- https://pymi.vn/tutorial/unicode/
