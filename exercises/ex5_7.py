#!/usr/bin/env python3


def solve(input_data):
    '''
    Trả về string biễu diễn tương ứng ở hệ thập phân (decimal),
    hệ nhị phân (binary), bát phân (octal), thập lục phân (heximal)

    Gợi ý: sử dụng bin(), oct(), hex(), string method `rjust`
    Mỗi dòng 1 số, với độ rộng là 8, các giá trị thẳng nhau căn lề phải.
    Output :

    .. code-block::

      .
      .
      15    1111    0o17     0xf
      16   10000    0o20    0x10
      17   10001    0o21    0x11
      18   10010    0o22    0x12
      19   10011    0o23    0x13
    '''

    result = None
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    raise NotImplementedError("Học viên chưa làm bài này")

    return result


def main():
    input_data = range(1, 20)
    print(solve(input_data))


if __name__ == "__main__":
    main()
