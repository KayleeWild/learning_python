'''
Week 8: For loops
Sister Hansen
'''

# 1) loop to print 1 through 5 (using a range)
for x in range(5):  
    print(x)
# loop to print odd values 1-11
print()
for x in range(1,12,2):
    print(x)

# 2) loop to print "Hello World" a user specified number of times
print()
repeat = int(input('How many times should we print Hello? '))
for x in range(repeat):
    print('Hello')

# 3) loop to print each letter in a string (two ways)
print()
my_string = "Hello"
# 1st way
print()
for letters in my_string:
    print(letters)
# 2nd way
print()
for i in range(len(my_string)):
    print(my_string[i])

# 4) loop to print each item in a list
print()
my_list = [1,3,5,7,9]
for numbers in my_list:
    print(numbers)

print()
for i in range(len(my_list)):
    print(my_list[i])



# team activity - looping through strings 


# a variation on the stretch
print()
first_name = "Brigham"
last_name = "Bounger"

# use range and len to loop through the string
for i in range(len(first_name)):
    # print(f"The letter {first_name[i]} is at position {i} in the first name")
    # print(f"The letter {last_name[i]} is at position {i} in the last name")
    # we could also use if statements to check if the letters are the same
    if first_name [i] == last_name [i]:
        print(first_name[i].upper(), end = '')
    elif first_name [i] in last_name:
        print(first_name[i].lower(), end = '')
    else:
        print('_', end= '')

print()
