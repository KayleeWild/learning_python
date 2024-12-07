number = -1 

while number < 0:
    number = int(input('Please type a positive number: '))
    if number < 0:
        print('Sorry, that is a negative number. Please try again.')
    else:
        print(f'The number is: {number}')


answer = 'no'

while answer != 'yes':
    answer = input('May I have a piece of candy? ')

if answer == 'yes':
    print('Thank you.')