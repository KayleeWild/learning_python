import random

play_again = 'yes'

while play_again.lower() == 'yes':
    guess = int(input('\nWhat is your guess? '))
    count = 1  
    magic = random.randint(1, 100)
    while guess != magic:
        if guess > magic:
            print('Lower')
        elif guess < magic:
            print('Higher')
        count += 1
        guess = int(input('What is your guess? '))
        
    print(f'You guessed it in {count} tries!')
    play_again = input('Do you want to play again? ')
print('Thnaks for playing! Bye now!')