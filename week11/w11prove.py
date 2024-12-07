'''
CSE110 - Week 11 Prove
Kaylee Wilding
'''
print()
max_expectancy = 0
min_expectancy = 9999
with open('week11/life-expectancy.csv') as file_var:
    header = next(file_var)
    for line in file_var:
        line = line.strip()

        line_list = line.split(',')
        entity = line_list[0]
        code = line_list[1]
        year = int(line_list[2])
        expectancy = float(line_list[3])

        if expectancy > max_expectancy:
            max_expectancy = expectancy

        if expectancy < min_expectancy:
            min_expectancy = expectancy

    print(max_expectancy)
    print(min_expectancy)
    