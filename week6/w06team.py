can_ride = False

print('\nStep right up! Step right up! Are you able to ride the ride?')

# This is the information for the first rider #
first_age = int(input('\nWhat is the age of the first rider? '))
if first_age < 18 and first_age >= 12:
     passport1 = str(input('Do you have a golden passport? '))
     if passport1.lower() == 'yes':
          first_age == 18
first_height = float(input('What is the height of the first rider? '))
second_rider = str(input('Is there a second rider (yes/no)? '))

# This is the information for the second rider, if applicable #
if second_rider.lower() == 'yes':
    second_age = int(input('What is the age of the second rider? '))
    if second_age < 18 and second_age >= 12:
     passport2 = str(input('Do you have a golden passport? '))
     if passport2.lower() == 'yes':
          second_age == 18
    second_height = float(input('What is the height of the second rider? '))
    if first_age >= 18 or second_age >= 18:
         can_ride = True
    elif first_age >= 12 and second_age >= 12 and first_height >= 52 and second_height >= 52:
         can_ride = True 
    elif (first_age >= 16 and second_age >= 14) or (first_age >= 14 and second_age >= 16):
         can_ride = True
    else:
          can_ride = False
     # Rule 1 #
    if first_height < 36 or second_height < 36:
          can_ride = False
    else:
        can_ride = True
else:
    if first_age >= 18 and first_height >= 62:
         can_ride = True
    else:
         can_ride = False

# So, can they ride? Let's find out #
if can_ride:
    print('Step right up! Step right up! You can ride the ride!!')
else:
     print('Sorry, you can\'t ride the ride today. Maybe next time try some soccer cleats and hair gel.')