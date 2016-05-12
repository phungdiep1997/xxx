def return_number_or_string(number):
    '''
    return number or string depends on input number
    '''

    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

for number in range(1,101):
    print(return_number_or_string(number))
