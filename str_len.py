#A Python program to calculate the length of a string

#Collects str value from console
string = input('Enter any string: ')

counter = 0 #As  the name implies

#counts through "string" chars
for i in string:
    counter = counter + 1
    
print('The length of the string is: ',counter)