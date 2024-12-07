# take a look at file.txt
# use best practice to open file.txt and store data in a file object
with open('week12/file.txt') as file_var:
    # if there's a header line, skip it
    # header = next(file_var)
    # header = file_var.readline()
    
    # loop through the lines (strings) in the file object
    for line in file_var:
        # strip whitespace and print line
        line = line.strip()
        print(line)
        # split line into parts (a list) and print list
        line_list = line.split(' ')
        print(line_list)
        # save parts in new variables so they're easier to use
        word1 = line_list[0]
        word2 = line_list[1]
        word3 = line_list[2]
        word4 = line_list[3]
