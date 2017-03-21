Exercises 4.x
=============

Bài 4.1
-------

Cho a, b, c là ba cạnh của tam giác vuông có chu vi 24 cm (perimeter).
Biết độ dài các cạnh <= 10cm.
Viết list comprehension để tìm các bộ a,b,c thoả mãn bài toán.

Bài 4.2
-------

Tính "điểm" cho từ:
(http://www.familug.org/2015/05/golang-tinh-tu-cung-9gag.html)

Nếu a b c d (không phân biệt chữ hoa thường) .... lần lượt bằng 1 2 3 4 ...

thì từ ``attitude`` có giá trị bằng 100

Tính giá trị của các từ:

Input: ['numpy', 'django', 'saltstack', 'discipline', 'Python', 'FAMILUG', 'pymi']

Output: list chứa "điểm" tương ứng của các từ.

Gợi ý::

  import string
  print string.ascii_lowercase

Bài 4.3
-------

Cho một list ``numbers`` chứa các số (kiểu int hoặc float), tìm phần tử lớn nhất trong list.
So sánh giá trị lớn nhất đó với max(numbers) bằng câu lệnh sau, nếu kết quả sai sẽ có exception
xảy ra::

  assert mymax == max(numbers), "wrong max"

Bài 4.4
-------

Giải bài toán lớp 3 có số đáp án khổng lồ
(http://www.familug.org/2015/05/codegolf-giai-bai-toan-lop-3-co-so.html)

Với các biến a,b,c,d,e,f,g,h,i là các số nằm trong khoảng 1-9 (các biến có thể
có giá trị giống nhau), dạng biểu thức:

    a + 13 * b / c + d + 12 * e – f – 11 + g * h / i – 10 = 66

In ra màn hình số nghiệm của bài toán.

Bài 4.5
-------

Cho list numbers chứa các giá trị từ -10 đến 10, trừ số 0.
In ra tuple chứa tổng (sum) và tích (product) của các phần tử trong list numbers.
Không sử dụng hàm ``sum``.

Input::

  li = range(-10, 11)
  li = list(li)
  li.remove(0)

Thêm dòng sau vào cuối bài để kiểm tra kết quả::

  from functools import reduce
  assert (mysum, myproduct) == sum(numbers), reduce(lambda x,y: x*y, numbers)

Bài 4.6
-------

Cho string s::

  s = 'Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu'

Tạo ra list numbers chứa tất cả các số trong string này theo thứ tự chúng xuất hiện trong ``s``.

Output::

  assert numbers == [60, 20, 0]

Bài 4.7
-------

Có 10 thiên can::

  ['giáp', 'ất', 'bính', 'đinh', 'mậu', 'kỷ', 'canh', 'tân', 'nhâm', 'quý']

Và 12 địa chi::

  ['tý', 'sửu', 'dần', 'mão', 'thìn', 'tị', 'ngọ', 'mui', 'thân', 'dậu',
   'tuất', 'hợi']

Biết năm 2017 là năm "Đinh Dậu", tạo list can_chi chứa tuple là cặp (năm, can chi) tương ứng
của các năm từ 2008 đến 2020.

Kiểm tra kết quả bằng dòng code sau::

assert can_chi == [(2008, 'Mậu Tý'), (2009, 'Kỷ Sửu'), (2010, 'Canh Dần'),
                   (2011, 'Tân Mão'), (2012, 'Nhâm Thìn'), (2013, 'Quý Tị'),
                   (2014, 'Giáp Ngọ'), (2015, 'Ất Mui'), (2016, 'Bính Thân'),
                   (2017, 'Đinh Dậu'), (2018, 'Mậu Tuất'), (2019, 'Kỷ Hợi'),
                   (2020, 'Canh Tý')]
