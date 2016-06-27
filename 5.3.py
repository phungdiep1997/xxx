li = [i for i in range(1,101)]

def auto_change(li):
    for i in range(1, len(li)):
        if i % 3 == 0:
            li[i - 1] = 'Fizz'
        if i % 5 == 0:
            li[i - 1] = 'Buzz'
        if i % 3 == 0 and i % 5 == 0:
            li[i - 1] = 'FizzBuzz'
    return li

print(auto_change(li))