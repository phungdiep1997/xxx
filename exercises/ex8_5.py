#!/usr/bin/env python3


__doc__ = '''Viết chương trình cứ 1 giây in ra màn hình thời gian hiện tại.

- Sau 60 lần thì chương trình kết thúc

- Hướng dẫn: time.sleep, datetime.datetime.now
'''

import time


def your_function():
    '''Trả về tuple chứa 2 phần tử bao gồm:
    - List chứa các điểm thời gian sau 60 lần thực hiện
    theo yêu cầu từ ``__doc__``
    - Tổng thời gian chạy của function

    Lưu ý:
    - Mỗi lần in ra màn hình thời gian hiện tại thì tiến hành thêm
    thời gian đó vào list

    :rtype tuple:
    '''
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    start = time.time()

    result = None
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError("Học viên chưa làm bài này")

    end = time.time()
    total_time = end - start
    return (result, total_time)


def solve():
    '''Học viên không cần chỉnh sửa trong hàm solve, chỉ thực hiện
    đổi tên lại function của mình cho phù hợp

    Hàm solve dùng cho mục đích `test`
    :rtype tuple:
    '''
    result = your_function()
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
