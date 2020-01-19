#A Python program to get a single string from two given strings,
#  separated by a space and swap the first two characters of each string

#Collects str values from console
first_string = input('Enter fist string: ')
second_string = input('Enter second string: ')

#To make sure inputed str has enough char
while (len(first_string) < 2) and (len(second_string) < 2):
    first_string = input('Enter fist string: ')
    second_string = input('Enter second string: ')
#Swaps the first 2 chars and get's the last char of each str
first_string_swap = second_string[:2] + first_string[-1]
second_string_swap = first_string[:2] + second_string[-1]

#Joins the swapped chars
new_string = first_string_swap + " " + second_string_swap
print(new_string)