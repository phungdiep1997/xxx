def sumall(*args):
    sum_ = 0
    for i in args:
        sum_ = sum_ + i
    return sum_

print(sumall(1,2,3,4,5,6,7))
print(sumall(1,2,3,4,5,6,7,8,9))