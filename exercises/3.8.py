#!/usr/bin/python

lst = [i for i in range(5, 1000, 5) if i % 3 == 0 and i % 5 == 0]

print(lst)

print(sum(lst))
