import os

months_list = ['January', 'February', 'March', 'April',  'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def day_of_month(month):
    months_dict = {31: ['January', 'March', 'May', 'July', 'August', 'October', 'December'], 30: ['April', 'June', 'September', 'November'], 28: ['February']}
    for d, m in months_dict.items():
        if month in m:
            day = d
    return day

with open(os.path.dirname(os.path.abspath(__file__)) + '64out.txt', 'w') as f:
    line_number = 1
    for month in months_list:
        f.write(str(line_number) + ', ' + month + ', ' + str(day_of_month(month)) + ' days\n')
        line_number += 1
        
with open(os.path.dirname(os.path.abspath(__file__)) + '64out.txt', 'r') as f:
    print(f.read())