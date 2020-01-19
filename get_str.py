#A Python program to get a string made of the first 2 and the last 2 chars from a given a string.

#Collects str value from console
string = input('Enter any string: ')

#To make sure inputed str has enough char
while (len(string) < 4):
    string = input('Enter any string: ')

#Collects the first 2 and the last 2 chars from "string" and joins them
new_string = string[0:2] + string[-2:]

print(new_string)#prints the new formed str to the console
