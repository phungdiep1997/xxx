fibonaci = [1, 2]
while 1:
    next_number = fibonaci[len(fibonaci)-2]+fibonaci[len(fibonaci)-1]
    if next_number > 4000000:
        break
    fibonaci.append(next_number)
result = sum(i for i in fibonaci if i % 2 == 0)
print(result)