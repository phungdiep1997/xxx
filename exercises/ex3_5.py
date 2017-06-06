#!/usr/bin/env python3

'''
- input_data = ["I", "Love", "You", "Chiu", "Chiu"]

- output: in ra thành cặp

Ví dụ::

  1 I
  2 Love
  3 You
  ... cho đến hết

Gợi ý: có thể dùng enumerate()
https://docs.python.org/2/library/functions.html#enumerate
'''


data = ["I", "Love", "You", "Chiu", "Chiu"]


def solve(input_data):
    '''Trả về 1 `list` các `list` theo định dạng sau:

        result = [[1, "I"], [2, "Love"], [3, "You"], [4, "Chiu"], [5, "Chiu"]]

    :rtype: list
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError("Học viên chưa làm bài này")

    return result


def main():
    for word in solve(data):
        for num, value in word:
            print(num, value)


if __name__ == "__main__":
    main()
