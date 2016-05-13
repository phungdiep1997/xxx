#!/usr/bin/python

str = 'xin chao cac ban'

lst = ["%s: %d" % (c, str.count(c)) for c in str]

lst = list(set(lst))
lst.sort()

print(', '.join(lst))
