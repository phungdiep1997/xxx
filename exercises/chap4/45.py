#!/usr/bin/python

from functools import reduce

def sum_and_product(numbers):
    '''
    sum and product of a integers list

    product_ = 1

    for num in numbers[numbers.index(1):]:
        product_ *= num

    return (0, product_ ** 2)
    '''

    sum_ = 0
    product_ = 1
    for number in numbers:
        sum_ += number
        product_ *= number

    return (sum_, product_)

numbers = list(range(-10, 11))
numbers.remove(0)

print(sum_and_product(numbers))

assert sum_and_product(numbers) == (sum(numbers), reduce(lambda x, y: x * y, numbers))
