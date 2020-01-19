#Learning Integer Literals 
birth_month = input('Enter birth month: ')
if type(birth_month) == str:
    print('Not an integer')
if type(birth_month) != int:
    print('Converting to int now.........')
    int(birth_month)
    print('....................')
    print('Now is of int type')
