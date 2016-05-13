#!/usr/bin/python3

import sys
import subprocess

def creat_file(filename, lines = 3000):
    '''
    create file and write data
    '''

    with open(filename, 'a+') as fd:

        count = 1

        while count <= lines:
            if count % 2 == 1:
                data = '1' * 30
            else:
                data = count * 2

            fd.write(str(data) + '\n')

            count += 1

def print_last_n_lines(filepath, line = 10):
    res = subprocess.Popen('tail -n %d %s' % (line, filepath), shell=True, stdout=subprocess.PIPE)
    print(res.communicate()[0].decode('utf-8'))

def get_file_size(filepath):
    try:
        fopen = open(filepath, 'r')
    except:
        sys.exit('can not open file')

    fopen.seek(0, 2)
    print(fopen.tell())

creat_file('/tmp/temp_file', lines=20)
print_last_n_lines('/tmp/temp_file', 10)
print(get_file_size('/tmp/temp_file'))
