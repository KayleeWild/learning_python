# WORDLE Game

secret = 'purple'
guess = None
count = 0

print('\nHello there! Welcome to knock-off Wordle!')
print('\nYour hint is: ', end= '')
for letter in secret:
    print('_ ', end= '')

while guess != secret:
    guess = input('\nWhat is your guess? ')
    count += 1
    if guess == secret:
        print(f'\nYou guessed it!\nIt took you {count} tries!')
    else:
        print('\nIncorrect. Try again please.')
        if len(guess) == len(secret):
            print('\nYour hint is: ', end='')
            for i in range(len(secret)):
                if secret [i] == guess.lower() [i]:
                    print(secret[i].upper(),'', end= '')
                elif guess.lower() [i] in secret:
                    print(guess[i].lower(),'', end= '')
                else:
                    print('_ ', end='')
        elif len(guess) > len(secret):
            print('Guess has too many letters. Try a 6-letter word.')
            print('\nYour hint is: _ _ _ _ _ _')
        else:
            print('Guess doesn\'t have enough letters. Try a 6-letter word.')
            print('\nYour hint is: _ _ _ _ _ _')