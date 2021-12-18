 #--- Python Mini Project - Library Management System -----
# Create list_of_books.txt file 
# List of books :

import datetime
import os
os.getcwd()

class LMS:
    print("""
    This class is used to keep records of books library.
    It has total four modules: 'Display Books', 'Lend Books', 'Add Books', 'Return Books'
    'list_of_books' should be txt file. 'library_name' should be string.
    """)

    def __init__(self, list_of_books, library_name):
        self.list_of_books = "list of books.txt"
        self.library_name = library_name
        self.books_dict = {}
        id = 101
        with open(self.list_of_books) as b:
            content = b.readlines()
        for line in content:
            print(line)
print(LMS("list of book.txt", "codewithme"))