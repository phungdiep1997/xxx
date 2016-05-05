#!/usr/bin/python

lst = []
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a + b / c == 10:
                lst.append([a, b, c])

print(lst)
