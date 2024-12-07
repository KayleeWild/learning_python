'''
Week 09 Prove
Shopping Cart
-Kaylee Wilding
'''

cart_items = []
item_prices = []
menu_choice = None

print('\nWelcome to the fake shopping cart! What would you like to do?')
while menu_choice != 'quit':
    print('\nMenu:')
    print('Add a new item')
    print('View cart')
    print('Remove an item')
    print('View cart total')
    print('Quit')
    menu_choice = input('\n')

    if menu_choice.lower() == 'add a new item':
        item = input('\nWhat item would you like to add? ')
        cart_items.append(item)
        price = float(input(f'What is the price of \'{item}\'? '))
        item_prices.append(price)
        print(f'\'{item}\' has been added to the cart.')

    elif menu_choice.lower() == 'view cart':
        print('\nThe contents of the shopping cart are:')
        for item in cart_items:
            print(item)

    elif menu_choice.lower() == 'remove an item':
        print('Good job Kaylee!')
    elif menu_choice.lower() == 'view cart total':
        print('Good job Kaylee!')
print('Thanks, have a happy day!')