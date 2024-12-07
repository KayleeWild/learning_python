grade = float(input('\nPlease enter your grade percentage: '))

if grade >= 90:
    print('You got an A!')
elif grade >= 80:
    print('You got a B.')
elif grade >= 70:
    print('You got a C.')
elif grade >= 60:
    print('You got a D.')
else:
    print('Oh no, you got an F!')

if grade >= 70:
    print('You passed! Yay!')
else:
    print('Looks like you\'ll be taking this class agian.')
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
grade = float(input('\nPlease enter your grade percentage again for a different way of calculating: '))
last_digit = grade % 10
if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'

if grade >= 97:
    sign = ''
elif letter == 'F':
    sign = ''
elif last_digit >= 7:
    sign = '+'
elif last_digit < 3:
    sign = '-'
else:
    sign = ''
print(f'Grade: {letter}{sign}!')

if grade >= 70:
    print('You passed! Yay!')
else:
    print('Looks like you\'ll be taking this class agian.')