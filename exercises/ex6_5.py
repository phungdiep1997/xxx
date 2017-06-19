#!/usr/bin/env python3

import os
import json # NOQA


data = os.path.join(os.path.dirname(__file__), 'salt_contributors.json')


def your_function(datapath):
    '''Trả về list chứa các dictionary chứa data về các contributor bao gồm
    các key: login, url và contributions.
    '''
    # Sửa function cho phù hợp, trả về kết quả yêu cầu.

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError("Học viên chưa làm bài này")


def solve(input_data):
    result = your_function(input_data)

    return result


def main():
    '''Truy cập đường dẫn
    https://api.github.com/repos/saltstack/salt/contributors?page=3 Lưu lại
    thành file salt_contributors.txt.
    Sử dụng JSON để chuyển dữ liệu thành dữ liệu trong Python.
    '''
    datafile = data

    print(solve(datafile))


if __name__ == "__main__":
    main()
