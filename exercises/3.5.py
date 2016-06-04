#!/usr/bin/python

month = 2

if month not in range(1,13):
    print('invalid month')

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

days = 28
if month in [1,3,5,7,8,10,12]:
    days = 31
elif month in [4,6,9,11]:
    days = 30

print('%s %s' % (months[month-1],days))
#print(months[month-1], days) # tai sao lai print ra tuple :D ('February', 28)
