#!/usr/bin/env python3


def solve_5_4(output_path):
    '''Tạo ra 1 file chứa 30 triệu dòng, các dòng lẻ chứa 30 số 1,
    các dòng chẵn chứa giá trị 2 * số dòng hiện tại.

    Sau khi tạo xong file, return result là list chứa 10 dòng đó theo thứ tự
    dòng xuất hiện trước đứng trước.

    Chú ý: để bài hoàn toàn chính xác.
    '''
    result = None
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    raise NotImplementedError("Học viên chưa làm bài này")

    return result


def main():
    import tempfile
    # tên _ hàm ý rằng ta sẽ không dùng giá trị của nó - convention
    _, output_path = tempfile.mkstemp()
    print('File to write: {0}'.format(output_path))
    for line in solve_5_4(output_path):
        print(line.rstrip())


if __name__ == "__main__":
    main()
