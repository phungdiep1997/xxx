#!/usr/bin/python

str = 'cho meo ga chuot vit ngan'

lst = [l for l in str if str.count(l) == 1]
print(lst)

''' # method 2
lst = []
for c in str:
    if str.count(c) == 1:
        lst.append(c)
print(lst)
'''
