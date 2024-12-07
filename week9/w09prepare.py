'''
Week 9 preparation
Kaylee Wilding
'''
print()

names = []

name = ''

while name != 'end':
    name = input('Type the name of a friend: ')

    if name != 'end':
        names.append(name)

print('\nYour friends are:')
for name in names:
    print(name)