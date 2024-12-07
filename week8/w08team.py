word = 'commitment'
favorite = input('What is your favorite letter? (c, o, m, i, t, n, or e) ')

print()
for letter in word:
    if letter.lower() == favorite.lower():
        print('_', end= '')
    else:
        print(letter.lower(), end='')
print()

