Exercises 5.x
======

Ex1
---

Viết lại tất cả các bài trong 3.X, 5.1 có sử dụng try/except để xử lý các lỗicó
thể xảy ra (Tất cả các funtion viết trong 1 file).


Ex2
---

Kiểm tra OS của máy đang dùng  xem có là Linux based OS không?

Hướng dẫn: sử dụng sys module.

https://docs.python.org/2/library/sys.html

Ex3
---

Write a function that prints the numbers from 1 to 100. But for multiples of
three print “Fizz” instead of the number and for the multiples of five print
“Buzz”. For numbers which are multiples of both three and five print
“FizzBuzz”.

Ex4
---

Viết function tạo ra 1 file chứa 30 triệu dòng, các dòng lẻ chứa 30 số 1,
các dòng chẵn chứa giá trị 2 * số dòng hiện tại.

Viết function in ra 10 dòng cuối cùng của file nói trên.

(Nâng cao) Viết function in ra kích thước của file nói trên tính theo byte.

Ex5
---

Using names.txt https://projecteuler.net/project/resources/p022_names.txt
(right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names, begin by sorting it
into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

https://projecteuler.net/problem=22


Ex6
---

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 10×10 grid?

Similar to https://projecteuler.net/problem=15

Ex7
---

In ra mà hình các biễu diễn tương ứng ở hệ thập phân (decimal), hệ cơ số nhị phân (binary), bát phân
(octal), thập lục phân (heximal) của các số từ 1 đến 20.

Gợi ý: sử dụng bin(), oct(), hex().
Mỗi dòng 1 số, với độ dài các cột bằng chiều dài của bin
Output :

.. code-block::

    decimal     octal           hex         bin
        1           1           1           1
        2           2           2           10
        3           3           3           11

Ex8
---

- In ra màn hình biểu diễn của 20 mã ASCII đầu tiên.
- In ra màn hình Unicode codepoint của các số từ 0->9, a-zA-Z.
- Các ký tự "\t" "\n", " " có codepoint là bao nhiêu?

Gợi ý: dùng ``chr()``, ``ord()``.
