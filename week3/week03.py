'''
Week 3: Variables and Expressions(math)
Sister Hansen
'''

#### Which are each of the following? (string, int, float)
x = '10'   #string
y = 5   #integer
z = 3.14   #float
print(x*5, y, z*2)

#### What do the following do?
x = int(x)  #converts to an integer
y = float(y)  #converts to a float
z = str(z)   #converts to a string

# print(x, y, z*2)

#### Which is better?
print("I have " + str(x) + " cats.")
print("I have", x, "cats.")
print(f"I have {x} cats.")

#### Order of operations
#### math operations and order of operations
'''
Operator	Description
()	        Parentheses
**	        Exponent
* / // %	Multiply, Divide, Floor divide, Modulo
+ -	        Addition, Subtraction
= 	        Assign
'''

#### What is stored in a, b, c and d? 
a = 10 + (4 * 2) - 3  #15
b = 5 % 2   #1
c = 5 // 2  #2
d = 5 / 2   #2.5
e = 2 / 2   #1
print(f'math {a}, modulo {b}, floor divide {c}, normal divide {d}, divide ints {e}')

#### Team Activity
## Core requirements: 
# get user input (be able to handle ints or floats)
# convert it to a number so you can do some math with it (float)
# calculate areas of 3 shapes

side = float(input('What\'s the length of one side: '))
