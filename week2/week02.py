'''
Week 2: More variables, input, and output
Sister Hansen
What kind of comment is this?
'''

#### variables (and good names) - What kind of comment is this?
# create a string variable
name = 'bill'

# create an integer variable
age = 10

# create a float variable
age = 3.5

#### input
# get input from the user and store it in a variable
name = input('Enter your name: ')

# get a number from the user (decide if you want to convert now or later)
age = input('Enter your age: ')
age = int(age)

#### output and f-strings
# output all the variables with a single print statement
print('Your name is', name,'your age is', age)

# now use an f-string to output all the variables
print(f'Your name is {name} and your age is {age}')

# output all the variables again, but use a string method on one 
# so that it prints in upper case, lower case, or title case

print(f'Your name is {name.upper()} and your age is {age}')

print('-' * 20)

