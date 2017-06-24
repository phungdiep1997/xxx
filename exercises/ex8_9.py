#!/usr/bin/env python3


__doc__ = '''
- Tìm và in ra số dòng trong tất cả các file trong thư mục hiện tại (bao gồm
cả thư mục con). In ra tổng số dòng của mỗi loại file (dựa vào phần mở rộng
abc.py và xyz.py là cùng loại). Nếu file đã đọc là python module, in ra màn
hình tên của các function trong đó. Chạy chương trình bằng lệnh:

    ex8_9.py thumuc

Gợi ý: sử dụng ó.walk để duyệt vào thư mục con.
'''


def solve():
    '''Trả về số dòng lấy được của tất cả các file .py trong thư mục
    kể cả thư mục con

    :rtype int:
    '''
    result = None

    # Xóa dòng sau và viết code vào đây set các gía trị phù hợp
    raise NotImplementedError("Học viên chưa làm bài này")

    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
