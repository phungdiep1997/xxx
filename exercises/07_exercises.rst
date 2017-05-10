Exercises 7.x
=============

Yêu cầu:

- Tất cả các bài tập phải viết vào một module riêng, trong mỗi file phải có dòng

``if __name__ == ...`` cuối mỗi file. (https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts)

- Tất cả các module đều phải là script (không yêu cầu với Windows) https://docs.python.org/3/tutorial/appendix.html#executable-python-scripts

7.1
---

https://docs.python.org/3/library/fractions.html

Thư viện fractions cung cấp class Fraction để tạo ra kiểu phân số trên Python.

Sử dụng Fraction để viết function sau::

  def sum_fraction(string1, string2):
      code_here
      return FLOAT_TYPE

  print(sum_fraction('1/3', '6/9'))

Tham khảo: http://www.familug.org/2017/03/python-fractions-tinh-toan-phan-so-tren.html

7.2
---

Viết 1 một trò chơi đánh đối kháng giữa 2 nhân vật. Mỗi nhân vật có tên, máu, vũ khí.
Vũ khí chọn random khi tạo nhân vật.

Viết 2 class để biểu diễn nhân vật và vũ khí:

    class Fighter(object):
        codehere

    class Weapon(object):
        codehere

Cho 2 nhân vật lần lượt đánh nhau, print kết quả mỗi lượt đánh, print người thắng.

7.3
---

Giả lập việc một người tiến lên hoặc lùi lại, biết xác suất người này tiến hay lùi đều là 50 %.
Với 100 trường hợp, tính tỷ lệ người này tiến lên phía trước với mỗi trường hợp.

Trường hợp 1: chỉ bước 1 bước
Trường hợp 2: bước 2 bước
...
Trường hợp 100: bước 100 bước

Output là list tỷ lệ người này tiến lên phía trước trong
100 trường hợp (ở dạng float, vd 50% là 0.5).

Đối với học viên học data science, yêu cầu sử dụng thư viện numpy để làm.

7.5
---

Viết chương trình thực hiện sự chuyển đổi sau:

  input: [a, abbbccccdddd, xxyyyxyyx]
  output: [a, abb3cc4dd4, xx2yy3xyy2x]

Giải thích: Những chữ cái không lặp lại thì output giữ nguyên chữ cái đó. Những
chữ cái liên tiếp sẽ in ra 2 lần + số lần lặp lại liên tiếp.

Đây là một biến thể của một thuật toán nén dữ liệu có tên Run-length encoding (RLE).

7.6
---

Biết dir(object) sẽ trả về tất cả thuộc tính (attribute) của object đó.
Module cũng là object.

In [11]: import os

In [12]: len(dir(os))
Out[12]: 284

Tìm:
- os nằm ở file nào?
- os và sys có chung các attribute nào?
- code file ứng với thư viện os có bao nhiêu dòng?

7.7
---

Khi một chương trình đang chạy, nếu bấm Ctrl-C sẽ tạo ra 1 exception KeyboardInterrupt::

	while True:
	    print(1)
	# bấm Ctrl C
	1
	...
	1
	^C1
	1
...
	---------------------------------------------------------------------------
	KeyboardInterrupt                         Traceback (most recent call last)
	<ipython-input-21-becd8c056cb9> in <module>()
	      1 while True:
	----> 2     print(1)
	      3


Viết script với try và except để xử lý khi người dùng bấm Ctrl C, chương trình vẫn
chạy bình thường.
Để đóng chương trình, dùng task manager và chọn python process đang dùng nhiều CPU nhất.
