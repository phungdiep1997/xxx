Hướng dẫn làm bài tập
=====================

Với mỗi bài tập, tạo một file với tên::

  tenhocvien_X.Y.py

Ví dụ học viên: Nguyễn Hải Nam làm bài 3.1 sẽ đặt tên file::

  namnh_3.1.py

Trường hợp có 2 người trùng tên hãy hỏi
giảng viên để biết thêm chi tiết.

Nội dung của file này chứa lời giải
của bài toán. Ví dụ với bài toán yêu cầu
in ra từ 1 đến 10, học viên viết vào
file vừa tạo với nội dung::

  for i in range(1,11):
      print i

Và chạy file này với lệnh::

  python2 namnh_3.1.py

Làm bài xong học viên lưu vào git::

  git add namnh_3.1.py
  git commit -m 'add'
