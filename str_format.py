""" Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead. 
If the string length of the given string is less than 3, leave it unchanged.
"""
#Collects str value from console
string = input('Enter any string: ')

if (len(string) <= 3):#Checks if the str meets requirements
    print('String too small',string)
elif 'ing' not in string[-3:]:#Checks if the keyword "ing" is in str
    string += 'ing'
    print(string)
else:
    string += 'ly'
    print(string)