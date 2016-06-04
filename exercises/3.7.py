#!/usr/bin/python

lst = ['%s == %d * 5' % (i, i/5) for i in range(5, 100, 5) if i % 5 == 0]

for l in lst:
    print(l)
