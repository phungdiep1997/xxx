#!/usr/bin/python

def return_max(a, b):
    '''
    return maximum number of a and b
    '''
    return a if a >= b else b

numbers = [1, 10.2, 6, 100, 29, 56.8, 200.3, 99]

max_num = numbers[0]

for number in numbers:
    max_num = return_max(max_num, number)

assert max_num == max(numbers)



