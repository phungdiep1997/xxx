#!/usr/bin/env python3

import random  # NOQA
import string  # NOQA


def your_function(length=16):
    '''Tạo một mật khẩu ngẫu nhiên (random password),
    mật khẩu này bắt buộc phải chứa ít nhất 1 chữ thường,
    1 chữ hoa, 1 số, 1 ký tự punctuation (string.punctuation).
    '''
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError("Học viên chưa làm bài này")


def solve(input_data):
    result = your_function(input_data)
    return result


def main():
    '''
    Sinh ra 10 password và viết code đảm bảo chúng đều khác nhau.
    '''
    passwords = [your_function(12) for _ in range(10)]
    assert len(set(passwords)) != 1

    N = 12
    print('Mậu khẩu tự tạo {0} ký tự của bạn là {1}'.format(N, solve(N)))


if __name__ == "__main__":
    main()
