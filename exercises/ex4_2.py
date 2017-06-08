#!/usr/bin/env python3

'''
Biết `0o644` là biểu diễn của giá trị `420` (hệ 10) trên hệ bát phân (8-Octal).
Phải cộng `0o644` thêm bao nhiêu (ở dạng Octal) để thu được `0o777` ? In ra màn
hình giá trị đó.

'''


def solve(octal):
    '''Trả về giá trị cần cộng thêm với octal để thu được 0o777

    Với người dùng Unix(Ubuntu, MacOS,...), mode của một file được biểu diễn ở
    dạng Octal, VD: 644, 400, 777...

    Gợi ý:

    In [1]: oct(73)
    Out[1]: '0o111'
    '''

    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError("Học viên chưa làm bài này")

    return result


def main():
    print(solve(0o644))


if __name__ == "__main__":
    main()
