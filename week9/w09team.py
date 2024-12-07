'''
Week 09 team activity
-Kaylee Wilding
'''
print()
# definitions
def Average(number_list):
    return sum(number_list) / len(number_list)
number_list = []
number = 1

# start of program
print('Enter a list of numbers, type 0 when finished.')

while number!= 0:
    number = int(input('Enter a number: '))
    if number != 0:
        number_list.append(number)

total = sum(number_list)
average = Average(number_list)
largest = max(number_list)

# outputs
print(f'The sum is: {total}')
print(f'The average is: {average}')
print(f'The largest number is: {largest}')
