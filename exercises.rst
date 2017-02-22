Exercises
=========

Hướng dẫn làm bài tập
---------------------

Tất cả bài tập phải làm vào trong thư mục ``exercises``, có thể tạo thư
mục con tuỳ ý, miễn là nằm trong ``exercises`` để được kiểm tra tự động.

Với mỗi bài tập, tạo một file với tên::

  X_Y.py

Ví dụ bài 3.1 sẽ đặt tên file::

  3_1.py

Nội dung của file này chứa lời giải của bài toán. Ví dụ với bài toán yêu cầu
in ra từ 1 đến 4, học viên viết vào file vừa tạo với nội dung::

  for i in range(1,5):
      print i

Và chạy file này với lệnh::

  python2 3_1.py

Copy và paste kết quả vào cuối file ``3_1.py``::

  # Result
  # 1
  # 2
  # 3
  # 4

Làm bài xong học viên lưu vào git::

  git add 3_1.py
  git commit -m 'add'


.. toctree::
   :caption: All Exercises Content
   :maxdepth: 2
   :glob:

   exercises/*

Additional exercises: https://www.hackerrank.com/domains/python/py-introduction
