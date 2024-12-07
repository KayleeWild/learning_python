'''
CSE110 - Week 12 Prove
Kaylee Wilding
'''
print()
# variables
max_expectancy = 0
max_entity = ''
max_year = 0
max_code = ''
max_year_expectancy = 0
max_year_entity = ''
min_expectancy = 9999
min_entity = ''
min_year = 9999
min_code = ''
min_year_expectancy = 9999
min_year_entity = ''
total_year_expectancy = 0
count = 0

interest_year = int(input('Enter the year of interest: '))

# file
with open('week12/life-expectancy.csv') as file_var:
    header = next(file_var)
    for line in file_var:
        line = line.strip()

        line_list = line.split(',')
        entity = line_list[0]
        code = line_list[1]
        year = int(line_list[2])
        expectancy = float(line_list[3])

        if expectancy < min_expectancy:
            min_expectancy = expectancy
            min_entity = entity
            min_year = year
            min_code = code

        if expectancy > max_expectancy:
            max_expectancy = expectancy
            max_entity = entity
            max_year = year
            max_code = code

        if year == interest_year:
            if expectancy > max_year_expectancy:
                max_year_expectancy = expectancy
                max_year_entity = entity

            if expectancy < min_year_expectancy:
                min_year_expectancy = expectancy
                min_year_entity = entity
            total_year_expectancy += expectancy
            count += 1
    
    average = total_year_expectancy / count
    print()
    print(f'The overall max life expectancy is: {max_expectancy} from {max_entity} in {max_year}. The country code is {max_code}')
    print(f'The overall min life expectancy is: {min_expectancy} from {min_entity} in {min_year}. The country code is {min_code}')
    print()
    print(f'For the year {interest_year}:')
    print(f'The average life expectancy across all countries was {average:.2f}')
    print(f'The max life expectancy was in {max_year_entity} with {max_year_expectancy}')
    print(f'The min life expectancy was in {min_year_entity} with {min_year_expectancy}')
