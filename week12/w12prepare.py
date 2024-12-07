people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

min_age = 999999
min_name = ''
for line in people:
    line = line.strip()
    line_list = line.split(' ')

    name = line_list[0]
    age = int(line_list[1])

    if age < min_age:
        min_age = age
        min_name = name

print(min_name, min_age)