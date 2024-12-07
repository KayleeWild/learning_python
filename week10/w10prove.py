'''
Week 10 Prove
Shopping Cart
-Kaylee Wilding
'''

cart_items = []
item_prices = []
menu_choice = None

print('\nWelcome to the fake shopping cart! What would you like to do?')
while menu_choice != 'quit' and menu_choice != '5':
    print('\nMenu:')
    print('1. Add a new item')
    print('2. View cart')
    print('3. Remove an item')
    print('4. View cart total')
    print('5. Quit')
    menu_choice = input('\n')

    if menu_choice.lower() == 'add a new item' or menu_choice == '1':
        item = input('\nWhat item would you like to add? ')
        cart_items.append(item)
        price = float(input(f'What is the price of \'{item}\'? (write as decimal, don\'t include $) '))
        item_prices.append(price)
        print(f'\'{item}\' has been added to the cart.')

    elif menu_choice.lower() == 'view cart' or menu_choice == '2':
        print('\nThe contents of the shopping cart are:')
        for i in range(len(cart_items)):
            print(f'{i+1}. {cart_items[i]} - ${item_prices[i]:.2f}')

    elif menu_choice.lower() == 'remove an item' or menu_choice == '3':
        remove = int(input('Which item would you like to remove? ')) - 1
        cart_items.remove(cart_items[remove])
        item_prices.remove(item_prices[remove])
        print('Item removed.')

    elif menu_choice.lower() == 'view cart total' or menu_choice == '4':
        total = 0
        for i in item_prices:
            total += i
        print(f'Total: ${total:.2f}')
print('Thanks, have a happy day!')
