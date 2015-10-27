Exercises 3.x
=============

Chú ý: do chưa học function nên mỗi bài
có đầu vào thì học viên có thể đặt biến::

  input = dauvao

Nếu đầu vào nằm trong 1 khoảng thì học viên
chọn bất kỳ 1 số trong khoảng đó.

Chú ý 2: Khi làm các bài tập trong chương
đề nghị không sử dụng câu lệnh "import" - tức không sử dụng
bất kỳ thư viện nào.

Bài 3.1
-------

Đầu vào: một số nguyên dương

Đầu ra: phần từ số 1 cuối cùng trở về bên
phải - của dạng binary của số đầu vào.

Ví dụ::

  input = 5 # (0b101)
  output = 1

  input = 24 (11000)
  output = 1000

  input = 9 (1001)
  output = 1

Hàm có sẵn: bin(10) == 1010

Bài 3.2
-------

- input: một số nguyên

- output: in ra màn hình:

Nếu số < 0: this is negative number

Nếu số = 0: this is zero

Nếu số > 0: this is positive number


Bài 3.3
-------
Viết chương trình loại bỏ phần mở rộng của một tên file bất kỳ.
Ví dụ::

  input = '....slsslslsls...sls'
  output = '....slsslslsls..'

  input = 'maria.ozawa.mp9'
  output = 'maria.ozawa'

Bài 3.4
-------

- input = range(5, 16)

- output: in ra thành cặp

Ví dụ::

  1 5
  2 6
  3 7
  ... cho đến hết

Gợi ý: có thể dùng enumerate()
https://docs.python.org/2/library/functions.html#enumerate

Bài 3.5
-------

Input: một số nguyên trong range(1,13).
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:

- input: 2

- output: February 28

Bài 3.6
-------

Viết chương trình nhận đầu vào là string "cho meo ga chuot vit ngan" và
in ra list chứa tất cả các chữ cái chỉ xuất hiện một lần trong string trên.

- input: names = "cho meo ga chuot vit ngan"

- output: ['m', 'e', 'u', 'v', 'i']

Bài 3.7
-------

Xét các số nguyên dương < 100, in ra các số chia hết cho 5 theo dạng::

    10 == 2 * 5
    15 == 3 * 5
    ...

Bài 3.8
-------

In ra list chứa các số nguyên dương nhỏ hơn 1000 chia hết cho cả 3 và 5

Tính tổng của các số đó.

Gợi ý: dùng hàm sum()

https://docs.python.org/2/library/functions.html#sum

Bài 3.9
-------

a, b, c là các số nguyên dương nhỏ hơn 10 và:

a + b/c = 10

In ra list chứa các bộ số thỏa mãn điều kiện trên (a, b, c có thể trùng nhau).

Ví dụ:

- output: [[9, 1, 1], ...]

Bài 3.10
--------

In ra 10 số nguyên tố đầu tiên trên cùng một dòng.

- Output: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29