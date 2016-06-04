#!/usr/bin/python

str = 'xin chao cac ban'

lst = [(c, str.count(c)) for c in str]

lst = list(set(lst))
lst.sort()

last_length = lst[0][1]
for char, length in lst:
    if length < last_length:
        break

    print('%s xuat hien nhieu nhat %d lan' % (char, length))




