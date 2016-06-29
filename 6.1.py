import os

def electricity_payment(quantity):
    if quantity <= 50:
        payment = 1230 * quantity
    elif quantity <= 100:
        payment = 1230 * 50 + (quantity - 50) * 1530
    else:
        payment = (1230 + 1530) * 50 + (quantity - 100) * 1786
    return payment

input_ = [1, 29, 1235, 69, 100]

def monthly_payment(*args):
    monthly_payment_li = []
    for i in args:
        for j in i:
            monthly_payment_li.append(electricity_payment(j))
    return monthly_payment_li
    
output_ = monthly_payment(input_)

with open(os.path.dirname(os.path.abspath(__file__)) + 'test.txt', 'a') as f:
    for i in output_:
        f.write(str(i) + ',')