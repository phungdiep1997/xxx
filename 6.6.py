input_ = str(112345666.789)

def format_number(number):
    number = number.replace('.', ',')
    integer_part = number.split(',')[0]
    if len(integer_part) % 3 == 0:
        tmp = [integer_part[i:i+3] for i in list(range(0,len(integer_part),3))]
        output = tmp[0]
        for i in list(range(1, len(tmp))):
            output = output + '.' + tmp[i]
        output = output + ',' + number.split(',')[1]
    elif len(integer_part) % 3 == 1:
        tmp1 = integer_part[:1]
        integer_part = integer_part[1:len(integer_part)]
        tmp = [integer_part[i:i+3] for i in list(range(0,len(integer_part),3))]
        output = tmp[0]
        for i in list(range(1, len(tmp))):
            output = output + '.' + tmp[i]
        output = tmp1 + '.' + output + ',' + number.split(',')[1]
    else:
        tmp1 = integer_part[:2]
        integer_part = integer_part[2:len(integer_part)]
        tmp = [integer_part[i:i+3] for i in list(range(0,len(integer_part),3))]
        output = tmp[0]
        for i in list(range(1, len(tmp))):
            output = output + '.' + tmp[i]
        output = tmp1 + '.' + output + ',' + number.split(',')[1]
    return output

print(format_number(input_))

