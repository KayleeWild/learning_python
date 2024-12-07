print()
# functions
def display_regular(message):
    print(message)
def display_uppercase(up_message):
    uppercase = up_message.upper()
    print(uppercase)
def display_lowercase(low_message):
    lowercase = low_message.lower()
    print(lowercase)

user_message = input('What is your message? ')
display_regular(user_message)
display_uppercase(user_message)
display_lowercase(user_message)