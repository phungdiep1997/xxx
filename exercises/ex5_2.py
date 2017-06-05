#!/usr/bin/env python3


def solve_5_2(input_data):
    '''Trả về list các tuple chứa cặp tên học viên và bạn gái.
    Nếu không có girl_friend thì đặt giá trị đó bằng string rỗng.
    '''
    result = None

    # Viết code vào đây set result làm kết quả
    #
    #
    #

    return result


def main():
    # Cho list chứa các dictionary chứa thông tin của các học viên:
    students = [
        {"name": "Hoang"},
        {"name": "Duy", "girl_friend": "Maria"},
        {"name": "Dai", "girl_friend": "Angela"},
        {"name": "Tu"},
    ]
    result = solve_5_2(students) # NOQA
    # In ra màn hình tên học viên kèm tên bạn gái (nếu có)


if __name__ == "__main__":
    main()
