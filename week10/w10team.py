'''
Week 10 Team Activity
Bank Accounts
-Kaylee Wilding
'''
print()

accounts = []
balances = []

print('Enter the names and balances of bank acounts (type: quit when done)')
account_name = 'purple party'
while account_name.lower() != 'quit':
    account_name =  input('What is the name of this account? ')
    if account_name.lower() != 'quit':
        accounts.append(account_name)
        balance = float(input('What is the balance? '))
        balances.append(balance)
print()

print('Account Information:')
for i in range(len(accounts)):
    print(f'{i + 1}. {accounts[i]} - ${balances[i]:.2f}')
print()

total = sum(balances)
print(f'Total: ${total:.2f}')
print(f'Average: ${(total / len(accounts)):.2f}')
high_index = balances.index(max(balances))
print(f'Highest balance: {accounts[high_index]} - ${max(balances)}')

update = 'yes'
while update.lower == 'yes':
    update = input('Do you want to update an account? ')
    if update.lower() == 'yes':
        change_number = input('Type the number of the account you wish to update: ')
        new_amount =