'''
Week 13 Team activity
Kaylee Wilding
'''
print()
import math

shape = ''
while shape.lower() != 'quit':
    shape = input('\n(Type quit to stop) What kind of shape do you have today? ')
    if shape.lower() == 'square':
        def compute_are_square(len_side):
            area = len_side ** 2
            return area
        side = float(input('Enter the length of a side: '))
        square_area = compute_are_square(side)
        print(f'The area of your square is {square_area}.')
    elif shape.lower() == 'rectangle':
        def compute_area_rectangle(len_width, len_length):
            area =  len_width * len_length
            return area
        width = float(input('\nEnter the width of the rectangle: '))
        length = float(input('Enter the length of the rectangle: '))
        rectangle_area = compute_area_rectangle(width, length)
        print(f'The area of your rectangle is {rectangle_area}.')
    elif shape.lower() == 'circle':
        def compute_area_circle(len_radius):
            area = math.pi * len_radius ** 2
            return area
        radius = float(input('\nEnter the radius: '))
        circle_area = compute_area_circle(radius)
        print(f'\nThe area of your circle is {circle_area}.')
    # elif shape.lower() != 'quit':
    #     print('I regret to inform you but we cannot perform your calculation for that specific shape.')
print('Have a good day.')