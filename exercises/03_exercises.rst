Exercises 3.x
=============

Chú ý: do chưa học function nên mỗi bài
có đầu vào thì học viên có thể đặt biến::

  input_data = dauvao

Nếu đầu vào nằm trong 1 khoảng thì học viên
chọn bất kỳ 1 số trong khoảng đó.

Chú ý 2: Khi làm các bài tập trong chương
đề nghị không sử dụng câu lệnh "import" - tức không sử dụng
bất kỳ thư viện nào.

3.3
---
In màn hình các số nguyên từ 1 đến 100, nhưng với bội của 3, in ra chữ "Fizz"
thay vì số đo. Với bội của 5, in ra chữ "Buzz" thay vì số đó. Với các số
là bội của cả 3 và 5 thì in ra chữ "FizzBuzz" thay vì số đó.


3.4
---
Viết chương trình loại bỏ phần mở rộng của một tên file bất kỳ.
Ví dụ::

  input_data = '....slsslslsls...sls'
  output = '....slsslslsls..'

  input_data = 'maria.data.mp9'
  output = 'maria.data'

3.5
---

- input_data = ["I", "Love", "You", "Chiu", "Chiu"]

- output: in ra thành cặp

Ví dụ::

  1 I
  2 Love
  3 You
  ... cho đến hết

Gợi ý: có thể dùng enumerate()
https://docs.python.org/2/library/functions.html#enumerate

3.6
---

Input: một số nguyên trong range(1,13).
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:

- input_data: 2

- output: February 28

Bài 3.7
-------

Xét các số nguyên dương < 100, in ra các số chia hết cho 5 theo dạng::

    5  == 1 * 5
    10 == 2 * 5
    15 == 3 * 5
    ...

Bài 3.8
-------

Tạo 1 list chứa các số nguyên dương nhỏ hơn 1000 là bội của 3 hoặc 5.

Tính tổng của các số đó.

Gợi ý: dùng hàm sum()

https://docs.python.org/3/library/functions.html#sum

Bài 3.9
-------

a, b, c là các số nguyên dương nhỏ hơn 10, biết a + b/c = 10

In ra list chứa các bộ số thỏa mãn điều kiện trên (a, b, c có thể trùng nhau).

Ví dụ:

- output: [[9, 1, 1], ...]

Bài 3.10
--------

In ra 10 số nguyên tố đầu tiên trên cùng một dòng.

- Output: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

Gợi ý: dùng print(2, end=', ')


Bài tập nâng cao
----------------

Bài 3.11
--------


  a) Viết 1 chương trình tìm kí tự xuất hiện nhiều nhất trong 1 chuỗi


  b) Viết 1 chương trình đếm số tần xuất hiện của các ki tự trong 1 chuỗi


  Ví dụ::


      'toi la aia' -->> t: 1, o: 1, i: 2, l: 1, a: 3


Bài 3.12
--------


  a) Viết 1 chương trình đổi 1 số từ cơ số 10 sang cơ số 16

    yêu cầu ko dùng hàm có sẵn


  b) Viết 1 chương trình:

  - input: 2 list A và B

  - output:

    - các phần tử cùng lúc xuất hiện trong 2 list

    - các phần tử chỉ có trong list A

    - các phần tử chỉ có trong list B

    - tất cả các phần tử trong list A và B

    - các phần tử chỉ có trong 1 list (A hoặc B)

3.13
----

Viết chương trình nhận đầu vào là string "cho meo ga chuot vit ngan" và
in ra list chứa tất cả các chữ cái chỉ xuất hiện một lần trong string trên.

- input: names = "cho meo ga chuot vit ngan"

- output: ['m', 'e', 'u', 'v', 'i']

Chuẩn bị cho buổi sau
---------------------

Cài một editor/IDE tuỳ thích.

Best IDE: Pycharm https://www.jetbrains.com/pycharm/ . No 1, không cần cãi 😎
Nhược điểm: nặng/ ngốn ram.

Best editor: KHÔNG TỒN TẠI. Gợi ý: [Sublime Text 3](http://www.sublimetext.com/)
hoặc [VS Code](https://code.visualstudio.com/download) (khác với VisualStudio to nặng).

Chưa đủ phê 😗 Vim (http://www.vim.org/download.php) hoặc Emacs (https://www.gnu.org/software/emacs/download.html)
