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

Tìm và in ra số dòng trong tất cả các file trong thư mục hiện tại (bao gồm cả thư mục con).
In ra tổng số dòng của mỗi loại file (dựa vào phần mở rộng abc.py và xyz.py là cùng loại).
Nếu file đã đọc là python module, in ra màn hình tên của các function trong đó.
Chạy chương trình bằng lệnh:

	type_check.py thumuc

Gợi ý: sử dụng os.walk để duyệt vào thư mục con.
