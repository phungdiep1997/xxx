#!/usr/bin/env python3


__doc__ = '''
Yêu cầu:
- Viết decorator in ra thời gian chạy của 1 function
'''

import time


def your_decorator(solve):
    '''Sử dụng function của bạn như 1 `decorator` tính thời gian chạy
    của function `solve`
    '''
    # Sửa lại tên và function cho phù hợp

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError("Học viên chưa làm bài này")


# Sửa tên decorator cho phù hợp
@your_decorator
def solve():
    '''Thực hiện 1 tính toán bất kì trong function `solve`

    Trả về kết quả tùy ý, gán lại vào `result`
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError("Học viên chưa thực hiện tính toán")
    time.sleep(10)
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
