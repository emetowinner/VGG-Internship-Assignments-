#A Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def is_caps(string):
    caps_counter = 0
    low_case_counter = 0
    for char in string:
        validator = char
        if (char == validator.upper()) and (char != ' '):
            caps_counter += 1
        elif (char == validator.lower()) and (char != ' '):
            low_case_counter += 1
        else:
            pass
    result = {'Lower Case':low_case_counter,'Upper Case':caps_counter}
    print(result)
    return result
#is_caps('Winner Is a python DeveloPer')


#A Python function to find the Max of three numbers
def max_num(*args):
    max_number = args[0]
    for num in args:
        if num >= max_number:
            max_number = num
    print(max_number)
    return max_number
#max_num(3,5,4,8,1,3,9)


#Write a Python function to find the Max of three numbers

def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
                break
            else:
                print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
#is_prime(6)
