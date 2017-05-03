Exercises 6
===========

6.1
---

Cho tiền điện sinh hoạt được tính theo công thức:

- 50 số đầu: 1230 VND/số.

- 50 số tiếp: 1530 VND/số.

- Các số tiếp theo: 1786 VND/số.

Tính tiền điện sinh hoạt với:

- Input: số điện sử dụng

- Ouput: số tiền phải trả

Yêu cầu thêm:

Cho đầu vào là một list chứa số điện tiêu thụ các tháng::

   [1, 29, 1235, 69, 100].

Tạo list chứa số tiền tương ứng phải trả.

6.2
---

Cho đầu vào::

  li = ['meo', 'bo', 'ga', 'cho', 'chim', 'gau']

Viết 1 dòng code Python (one-liner) để thu được list sau ::

   [('meo', 'bo'), ('ga', 'cho'), ('chim', 'gau')]

6.3
---

Viết code ghi ra file dates.csv, mỗi dòng chứa thứ tự, tên tháng bằng tiếng
Anh, và số ngày trong tháng đó (tháng 2 tính 28 ngày).

E.g::

  1, January, 31
  2, February, 28
  ...

Đọc file này vào rồi dùng csv.DictReader() để in giá trị tháng và ngày ở từng dòng
ra màn hình::

	import csv
	f = open('dates.csv')
	dr = csv.DictReader(f, ['index', 'month', 'days'])
	for line in dr:
	    print(line['month'], line['days'])
	f.close()

6.4
---

Viết một hàm đệ quy (recursive function) in ra từ 1 đến n:

  def rprint(n):
      code_here...

6.5
---

Mỗi số (term) mới trong chuỗi (sequence) Fibonacci được tạo ra bằng cách cộng 2
số trước đó. Bắt đầu với 1 và 2, 10 số đầu sẽ là:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Kiểm tra tất cả các số trong chuỗi Fibonacci mà giá trị < 4 triêu, tính tổng của
các số chẵn (sum of the even-valued terms).

Kiểm tra kết quả tại: https://projecteuler.net/problem=2

6.6
---

Viết function nhận đầu vào là 1 giá trị float, trả về 1 string biểu diễn số đó ở dạng:

1.123.456,789 khi nhận đầu vào là 1123456.789

Function có khả năng xử lý đầu vào là số float tuỳ ý.

6.7
---

Viết function ``sumall`` tính tổng của tất cả các argument được gọi.
Chạy function này với các argument dưới::

  sumall(1,2,3,4,5,6,7)
  sumall(1,2,3,4,5,6,7,8,9)

6.8
---

Viết 1 script sinh một mật khẩu ngẫu nhiên (random password),
mật khẩu này bắt buộc phải chứa ít nhất 1 chữ thường,
1 chữ hoa, 1 số, 1 ký tự punctuation (string.punctuation).
Sinh ra 10 password và viết code đảm bảo chúng đều khác nhau.

6.9
---

Biết dir(5) trả về list các attribute của object 5 (gồm cả method).
dir([]) trả về list các attribute của object empty list (list rỗng).

- Tìm các method mà cả list và int object đều có
- Tìm các method chỉ list object có
- Tìm các method chỉ int object có

6.10
----

Truy cập đường dẫn https://api.github.com/repos/saltstack/salt/contributors?page=3
Lưu lại thành file salt.txt. Sử dụng JSON để chuyển dữ liệu thành dữ liệu trong
Python.
Với mỗi phần tử trong list, in ra login, url và contributions.


11
--

`map` là một built-in function trong Python, nó nhận vào 1 function và 1
iterable (list, str), rồi trả về một iterable tương ứng, sau khi biến đổi mỗi
phần tử của iterable đó bằng function được gọi::

  In [1]: map(abs, [-1, -3, 4, 5])  # abs trả về giá trị tuyệt đối của số
  Out[1]: <map at 0x1121db6d8>

  In [2]: list(map(abs, [-1, -3, 4, 5]))
  Out[2]: [1, 3, 4, 5]

Viết function `mymap` bắt chước function `map`::

  def mymap(func, iterable):
      codehere

6.12
----

Viết hàm đệ quy (recursive function) giải bài toán tháp Hà Nội lừng danh
(https://en.wikipedia.org/wiki/Tower_of_Hanoi
hoặc https://vi.wikipedia.org/wiki/Th%C3%A1p_H%C3%A0_N%E1%BB%99i).

::

	def hanoi_tower(n):
	    code_here

In ra từng bước chuyển đĩa.

6.12
----

- Tạo một GitLab public repo, chứa file README.rst
  Trong file này, viết mô tả một sản phẩm CỤ THỂ bạn muốn làm được sau khoá học.
  Print link đến repo trong file code 6_12.py

Chuẩn bị cho buổi sau
---------------------

- Chạy python3 -m venv env
- Xem trong thư mục ``env`` vừa tạo có gì.
  https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments
- Dùng pip cài đặt các thư viện phổ biến::

  ```
  pip install requests six pep8 flake8 ipython ipdb numpy pandas scipy matplotlib jupiter flask
  ```
