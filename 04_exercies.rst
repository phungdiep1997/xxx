Bài 4.1
-------

Cho a, b, c là ba cạnh của tam giác vuông có chu vi 24 cm (perimeter).
Biết độ dài các cạnh <= 10cm.
Viết list comprehension để tìm các bộ a,b,c thoả mãn bài toán.

Bài 4.2
-------

Tính "điểm" cho từ:
(http://www.familug.org/2015/05/golang-tinh-tu-cung-9gag.html)

Nếu a b c d .... lần lượt bằng 1 2 3 4 ...

thì từ ``attitude`` có giá trị bằng 100

Tính giá trị của các từ:

Input: ["masturbation", pussy", "discipline", "beer", "familug"]

Output: list chứa "điểm" tương ứng của các từ.

Gợi ý::

  import string
  print string.ascii_lowercase

Bài 4.3
-------

Given a list of numbers (float or int), find the biggest element in that list.
Compare output with max(li)::

  assert mymax(li) == max(li)

Bài 4.4
-------

Giải bài toán lớp 3 có số đáp án khổng lồ
(http://www.familug.org/2015/05/codegolf-giai-bai-toan-lop-3-co-so.html)

Với các biến a,b,c,d,e,f,g,h,i là các số nằm trong khoảng 1-9 (các biến có thể
có giá trị giống nhau), dạng biểu thức:

    a + 13 * b / c + d + 12 * e – f – 11 + g * h / i – 10 = 66

Bài toán có tất cả bao nhiêu nghiệm?
