with open('week11/books.txt') as books_file:
    print()
    for line in books_file:
        book = line.strip()
        print(book)
    print()