#!/usr/bin/env python3


def solve_5_8():

    '''Trả về biểu diễn của 20 mã ASCII đầu tiên theo format
    [(1, BIEUDIENCUA1), ...]
    Unicode codepoint của các số từ 0->9, a-z, A-Z.
    Unicode codepoint tương ứng với ký tự ``\t`` ``\n``, `` ``

    Gợi ý: dùng ``chr()``, ``ord()``.
    '''
    tabcodepoint = None
    newlinecodepoint = None
    spacecodepoint = None
    twenty_ascii = []
    unicodes = []

    # Xoá dòng raise và Viết code vào đây set các giá trị phù hợp
    raise NotImplementedError("Học viên chưa làm bài này")

    result = (twenty_ascii, unicodes, tabcodepoint,
              newlinecodepoint,
              spacecodepoint)
    return result


def main():
    for part in solve_5_8():
        print(part)


if __name__ == "__main__":
    main()
