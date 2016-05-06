#!/usr/bin/python

lst = [(a, b, c) for a in range(1, 11) for b in range(1, 11) for c in range(1, 11) if a + b + c == 24]

print(lst)
