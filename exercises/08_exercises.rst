Exercises 8
===========

8.1
---

Lưu file https://raw.githubusercontent.com/hvnsweeting/states/master/salt/event/init.sls về máy với
tên event.yaml
Dùng pip cài thư viện PyYAML, import yaml và dùng yaml.load để biến nội dung trong file thành
kiểu dữ liệu trên Python.
In ra len của kiểu dữ liệu vừa tạo. Dùng thư viện json để pickle.dump nội dung, ghi ra một file
tên là event.json
Dùng thư viện pickle và pickle.dump nội dung trên ra file event.pkl. Chú ý khi mở file,
phải mở ở chế độ 'wb' để ghi ở dạng binary.

In ra kích thước của mỗi file đã tạo.

Gợi ý: sử dụng os.stat(filename).st_size

8.2
---

Viết script head_tail.py, khi gọi với -h và tên file sẽ in ra 10 dòng đầu tiên của file,
khi gọi với -t và tên file sẽ in ra 10 dòng cuối cùng của file.

Usage::

  head_tail.py -h file_path

  Print 10 first lines of file_path

  head_tail.py -t file_path

  Print 10 last lines of file_path

Use ``sys.argv``

8.3
---

Cho ``words = ['nhung', 'bong', 'hoa', 'nho']``, viết chương trình in ra
mỗi phần tử trong list mà không sử dụng for, không dùng list index.


Gợi ý:

- iterator, while, try/except

8.4
--- 

Viết decorator in ra thời gian chạy của 1 function::

  def timer(func, bravo=False):
      codehere
      if bravo:
          print("Hoan hô giỏi quá")

  @timer
  def foo():
      import time
      time.sleep(10)

  foo()

8.5
---

Viết chương trình cứ 60 giây in ra màn hình thời gian hiện tại.

Hướng dẫn: time.sleep, datetime.datetime.now

8.6
---

Kiểu dữ liệu collections.Counter giúp cho việc đếm trờ nên rất dễ dàng.

https://docs.python.org/3/library/collections.html#collections.Counter

Cho đoạn văn bản sau::
  
  s = 'A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.'

Tìm tần suất xuất hiện của mỗi từ. In ra màn hình 3 từ xuất hiện nhiều nhất, cùng số lần xuất hiện.

8.7
---

Viết một chương trình log ra màn hình:
- "started" - ở level INFO, khi chương trình đã chạy
- Thực hiện ghi ra đường dẫn /var/lib/pyfml/data.txt, bắt exception xảy ra và 
  log ở level ERROR nội dung của exception.
- "running" - ở level DEBUG, sau mỗi 5 s

- Sau 1 phút, log ra màn hình dòng "exiting..." rồi kết thúc chương trình.

8.8
---

Tìm và in ra số dòng trong tất cả các file trong thư mục hiện tại (bao gồm cả thư mục con).
In ra tổng số dòng của mỗi loại file (dựa vào phần mở rộng abc.py và xyz.py là cùng loại).
Nếu file đã đọc là python module, in ra màn hình tên của các function trong đó.
Chạy chương trình bằng lệnh:

	type_check.py thumuc

Gợi ý: sử dụng os.walk để duyệt vào thư mục con.