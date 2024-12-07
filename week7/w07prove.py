# WORDLE Game

secret = 'purple'
guess = None
count = 0

print('\nHello there! Welcome to knock-off Wordle!')

while guess != secret:
    print('\nYour hint is: _ _ _ _ _ _')
    guess = input('What is your guess? ')
    count += 1
    print('\nIncorrect. Try again please.')
print(f'You guessed it!\nIt took you {count} tries!')