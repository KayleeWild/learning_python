first = int(input('\nPlease enter an integer: '))
second = int(input('Now for another one: '))
if first > second:
    print('The first number is greater.')
else:
    print('The first number is not greater')
if first == second:
    print('The numbers are equal.')
else:
    print('The numbers are not equal.')
if first < second:
    print('The second number is greater.')
else:
    print('The second number is not greater.')

animal = input('\nWhat is your favorite animal? ')
if animal.lower() == 'elephant':
    print('That\'s my favorite animal too!')
else:
    print('That one is not my favorite.')