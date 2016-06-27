import os
li = []

#creat file
with open('/home/thinhcm/Desktop/pyfml1606/test.txt', 'w') as f:
    for i in range(1, 30000001):
        if i % 2 == 0:
            written_value = str(2 * i) + '\n'
        else:
            written_value = '1' * 30 + '\n'
        li.append(written_value)
    f.writelines(li)

#display the last ten lines
def display_ten_lines(file):
    line = file.readlines()
    total_of_lines = sum(1 for i in line)
    for i in range(1, total_of_lines):
        if i >= total_of_lines - 10:
            print(line[i])

with open('/home/thinhcm/Desktop/pyfml1606/test.txt') as f:
    display_ten_lines(f)

#determining the size of file in byte
def size_of_file(file):
    file.seek(0,2)
    size = file.tell()
    return size
with open('/home/thinhcm/Desktop/pyfml1606/test.txt') as f:
    print(size_of_file(f))