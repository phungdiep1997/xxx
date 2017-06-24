#!/usr/bin/env python3

__doc__ = '''
- Cho ``words = ['nhung', 'bong', 'hoa', 'nho']``, in ra mỗi phần tử trong
list mà không sử dụng for, không dùng list index.

Gợi ý:
    iterator, while, try/except
'''


import os

words = ['nhung', 'bong', 'hoa', 'nho']


def your_function(input_data):
    '''Trả về list chứa các dòng sau khi đọc từ file

    Lưu ý:
        - Ghi vào 1 file tên `spam.abc`

        - Với input_data truyền vào, tiến hành ghi từng từ vào trong file,
        mỗi từ 1 dòng

        - Sau khi ghi vào file, mở lại file đó, trả về list chứa các dòng
        sau khi đọc từ file

    Chú ý:
        - Không dùng for, không dùng list index.

    :param input_data: dữ liệu sử dụng (words)
    :rtype list:
    '''
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    result = None

    # Xóa dòng sau và viết code vào đây set các gía trị phù hợp
    raise NotImplementedError("Học viên chưa thực hiện ghi kết quả vào file")

    # Không cần chỉnh sửa những dòng bên dưới
    # Xoá file sau khi đã thực hiện thêm từng dòng trong file vào list
    try:
        os.remove('spam.abc')
    except OSError as e:
        print(e)

    return result


def solve(input_data):
    # function `solve` dành cho mục đích test, không cần sửa
    # Gía trị trả về của `solve` và `your_function` là như nhau
    result = your_function(input_data)

    return result


def main():
    data = words
    result = solve(data)

    # Viết đoạn code in ra mỗi phần tử trong list `result` ngay bên dưới
    # không dùng for, không dùng list index
    # Xóa dòng sau và viết code vào đây set các gía trị phù hợp
    raise NotImplementedError("Học viên chưa làm bài này")


if __name__ == "__main__":
    main()
