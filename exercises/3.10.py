#!/usr/bin/python

lst = [2, 3]
for i in range(4, 100):
    if len(lst) == 10:
        break

    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False

    if is_prime:
        lst.append(i)

print(lst)
#print('2, 3, 5, 7, 11, 13, 17, 19, 23, 29')
