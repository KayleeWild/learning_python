print('Please enter the items of the shopping list (type: quite to finish):')

shopping = []
item = 'turkey'

while item.lower() != 'quit':
    item = input('Item: ')

    if item.lower() != 'quit':
        shopping.append(item)

print('\nThe shopping list is:')
for item in shopping:
    print(item)

print('\nThe shopping list with indexes is:')
for i in range(len(shopping)):
    print(f'{i}. {shopping[i]}')

change = int(input('\nWhich item would you like to change? '))
new_item = input('What is the new item? ')

shopping[change] = new_item

print('\nThe shopping list with indexes is:')
for i in range(len(shopping)):
    print(f'{i}. {shopping[i]}')