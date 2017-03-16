Exercises 5.x
=============

Ex1
---

Biết mã hex của các màu trong Google logo là:

Xanh lá: #3cba54
Vàng: #f4c20d
Đỏ: #db3236
Xanh da trời: #4885ed

Biết cách để tạo chữ G màu xanh da trời dùng code HTML sau::

  <span style="color:#4885ed">G</span>

Viết code python in ra màn hình (hoặc ghi ra file index.html)
code HTML để tạo ra logo của Google với màu sắc chính xác.

Mở file này bằng trình duyệt web để xem kết quả.

Ex2
---

Kiểm tra OS của máy đang dùng xem có là Linux based OS không?

Hướng dẫn: sử dụng sys module.

https://docs.python.org/2/library/sys.html

Ex3
---

In màn hình các số nguyên từ 1 đến 100, nhưng với bội của 3, in ra chữ "Fizz"
thay vì số đo. Với bội của 5, in ra chữ "Buzz" thay vì số đó. Với các số
là bội của cả 3 và 5 thì in ra chữ "FizzBuzz" thay vì số đó.

Ex4
---

Viết code tạo ra 1 file chứa 30 triệu dòng, các dòng lẻ chứa 30 số 1,
các dòng chẵn chứa giá trị 2 * số dòng hiện tại.

Sau khi tạo xong file, đọc file và in ra 10 dòng cuối cùng của file nói trên.

(Nâng cao) Viết code in ra kích thước của file nói trên tính theo byte.

Ex5
---

Sử dụng file names.txt https://projecteuler.net/project/resources/p022_names.txt
(chuột phải và chọn 'Save Link/Target As...'), đó là file text nặng 46K,
chứa hơn 5000 từ. Đầu tiên hãy sắp xếp các từ này theo thứ tự bảng chữ cái
(alphabetical). Sau đó tính giá trị cho mỗi từ, nhân giá trị này với thứ tự của nó
trong list đã sắp xếp để thu được điểm của từ này.

Ví dụ, khi list đã được sắp xếp theo thứ tự bảng chữ cái, COLIN, có giá trị là
 3 + 15 + 12 + 9 + 14 = 53, và đó là từ thứ 938 trong list.

Vì vậy, COLIN có điểm là 938 × 53 = 49714.

Tổng điểm của tất cả các từ trong file là bao nhiêu?

Kiểm tra kết quả bằng https://projecteuler.net/problem=22


Ex6
---

Bắt đầu từ góc trên bên trái của ô có kích thước 2x2, và chỉ cho phép di chuyển
sang phải hoặc xuống dưới, có chính xác 6 đường để đi đến góc dưới bên phải.

Có bao nhiêu đường như vậy trong ô 10x10?

Kiểm tra kết quả bằng https://projecteuler.net/problem=15

Ex7
---

In ra mà hình các biễu diễn tương ứng ở hệ thập phân (decimal), hệ cơ số nhị phân (binary), bát phân
(octal), thập lục phân (heximal) của các số từ 1 đến 20.

Gợi ý: sử dụng bin(), oct(), hex().
Mỗi dòng 1 số, với độ rộng các cột bằng số ký tự trong biểu diễn nhị phân.
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

Ex9
---

Cho dữ liệu đầu vào như sau:

.. code-block::

    provinces = [
                {'name':'An Giang','population':2153700,'area':3536.7,'senator':10},
                {'name':'Bà Rịa - Vũng Tàu','population':1039200,'area':1989.5,'senator':6},
                {'name':'Bạc Liêu','population':873400,'area':2468.7,'senator':6},
                {'name':'Bắc Kạn','population':301000,'area':4859.4,'senator':6},
                {'name':'Bắc Giang','population':1588500,'area':3848.9,'senator':8},
                {'name':'Bắc Ninh','population':1079900,'area':822.7,'senator':6},
                {'name':'Bến Tre','population':1258500,'area':2357.7,'senator':7},
                {'name':'Bình Dương','population':1748000,'area':2694.4,'senator':8},
                {'name':'Bình Định','population':1501800,'area':6050.6,'senator':8},
                {'name':'Bình Phước','population':912700,'area':6871.5,'senator':6},
                {'name':'Bình Thuận','population':1193500,'area':7812.8,'senator':7},
                {'name':'Cà Mau','population':1217100,'area':5294.9,'senator':7},
                {'name':'Cao Bằng','population':515200,'area':6707.9,'senator':6},
                {'name':'Cần Thơ','population':1214100,'area':1409,'senator':7},
                {'name':'Đà Nẵng','population':973800,'area':1285.4,'senator':6},
                {'name':'Đắk Lắk','population':1796700,'area':13125.4,'senator':9},
                {'name':'Đắk Nông','population':543200,'area':6515.6,'senator':6},
                {'name':'Đồng Nai','population':2720800,'area':5907.2,'senator':11},
                {'name':'Đồng Tháp','population':1676300,'area':3377,'senator':8},
                {'name':'Điện Biên','population':519300,'area':9562.9,'senator':6},
                {'name':'Gia Lai','population':1342700,'area':15536.9,'senator':7},
                {'name':'Hà Giang','population':758000,'area':7914.9,'senator':6},
                {'name':'Hà Nam','population':790000,'area':860.5,'senator':6},
                {'name':'Hà Nội','population':6844100,'area':3323.6,'senator':30},
                {'name':'Hà Tĩnh','population':1230500,'area':5997.8,'senator':7},
                {'name':'Hải Dương','population':1735100,'area':1656,'senator':9},
                {'name':'Hải Phòng','population':1904100,'area':1523.9,'senator':9},
                {'name':'Hòa Bình','population':806100,'area':4608.7,'senator':6},
                {'name':'Hậu Giang','population':769700,'area':1602.5,'senator':6},
                {'name':'Hưng Yên','population':1145600,'area':926,'senator':7},
                {'name':'TP. Hồ Chí Minh','population':7681700,'area':2095.6,'senator':30},
                {'name':'Khánh Hòa','population':1183000,'area':5217.7,'senator':7},
                {'name':'Kiên Giang','population':1726200,'area':6348.5,'senator':9},
                {'name':'Kon Tum','population':462400,'area':9689.6,'senator':6},
                {'name':'Lai Châu','population':397500,'area':9068.8,'senator':6},
                {'name':'Lào Cai','population':646800,'area':6383.9,'senator':6},
                {'name':'Lạng Sơn','population':744100,'area':8320.8,'senator':6},
                {'name':'Lâm Đồng','population':1234600,'area':9773.5,'senator':7},
                {'name':'Long An','population':1458200,'area':4492.4,'senator':8},
                {'name':'Nam Định','population':1836900,'area':1652.6,'senator':9},
                {'name':'Nghệ An','population':2952000,'area':16490.9,'senator':13},
                {'name':'Ninh Bình','population':915900,'area':1376.7,'senator':6},
                {'name':'Ninh Thuận','population':576700,'area':3358.3,'senator':6},
                {'name':'Phú Thọ','population':1335900,'area':3533.4,'senator':7},
                {'name':'Phú Yên','population':877200,'area':5060.6,'senator':6},
                {'name':'Quảng Bình','population':857900,'area':8065.3,'senator':6},
                {'name':'Quảng Nam','population':1450100,'area':10438.4,'senator':8},
                {'name':'Quảng Ngãi','population':1227900,'area':5153,'senator':7},
                {'name':'Quảng Ninh','population':1177200,'area':6102.3,'senator':7},
                {'name':'Quảng Trị','population':608100,'area':4739.8,'senator':6},
                {'name':'Sóc Trăng','population':1301900,'area':3311.6,'senator':7},
                {'name':'Sơn La','population':1134300,'area':14174.4,'senator':7},
                {'name':'Tây Ninh','population':1089900,'area':4039.7,'senator':6},
                {'name':'Thái Bình','population':1868800,'area':1570,'senator':9},
                {'name':'Thái Nguyên','population':1150200,'area':3534.7,'senator':7},
                {'name':'Thanh Hóa','population':3426600,'area':11132.2,'senator':16},
                {'name':'Thừa Thiên - Huế','population':1114500,'area':5033.2,'senator':7},
                {'name':'Tiền Giang','population':1692500,'area':2508.3,'senator':8},
                {'name':'Trà Vinh','population':1015300,'area':2341.2,'senator':6},
                {'name':'Tuyên Quang','population':738900,'area':5867.3,'senator':5},
                {'name':'Vĩnh Long','population':1033600,'area':1504.9,'senator':6},
                {'name':'Vĩnh Phúc','population':1020600,'area':1236.5,'senator':6},
                {'name':'Yên Bái','population':764400,'area':6886.3,'senator':7}
    ]


Dùng list comprehensions để:

- Tạo 1 list chứa tên, dân số của các thành phố có tên bắt đầu bằng chữ H.

- Tạo 1 list chứa tên, dân số của các thành phố có dân số trên 1 triệu.

Ex10
----

Viết một function nhận đầu vào là một chữ cái hoặc số, trả về "morse code" (https://en.wikipedia.org/wiki/Morse_code) tương ứng.
