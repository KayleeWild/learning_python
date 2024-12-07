'''
Week 12 Team Activity
Kaylee Wilding
'''
print()
import string
max_chapter = 0
max_book = 0
scripture_choice = input('Which volume of scriptures would you like to learn about? ')
with open('week12/books_and_chapters.txt') as file_var:
    for line in file_var:
        # strip whitespace and print line
        line = line.strip()
        # print(line)
        # split line into parts (a list) and print list
        line_list = line.split(':')
        # print(line_list)

        # save parts in new variables so they're easier to use
        book = line_list[0]
        chapter = int(line_list[1])
        scripture = line_list[2]

        if scripture == scripture_choice:
            print(f'Scripture: {scripture}, Book: {book}, Chapters: {chapter}')
            if chapter > max_chapter:
                max_chapter = chapter
                max_book = book

    print(max_book, max_chapter)