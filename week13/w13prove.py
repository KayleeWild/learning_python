'''
Week 13 Prove
Kaylee Wilding
'''
print()
# Variables
temperature = float(input('What is the temperature? '))
unit = input('Fahrenheit of Celsius (F/C)? ')
wind_speed = 1
# Functions
def calc_wind_chill(temperature, wind_speed):
    wind_chill = 35.74 + (0.6215 * temperature) - (35.75 * wind_speed ** 0.16) + (0.4275 * temperature * wind_speed ** 0.16)
    return wind_chill
def convert_unit(temperature):
    if unit.upper() == 'C':
        new_temp = temperature * 9 / 5 + 32
    elif unit.upper() == 'F':
        new_temp = temperature
    return new_temp
# Calculations
new_temp = convert_unit(temperature)
# Wind Chill Loop
for wind_speed in range(5, 61, 5):
    wind_chill = calc_wind_chill(new_temp, wind_speed)
    print(f'At temperature {new_temp}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}')