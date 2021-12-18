import datetime
import os
os.getcwd

              #DISPLAY THE BOOK LIST THAT ARE AVAILABLE IN LIBRARY

class Library:
    print('''\nWELCOME TO LUFFY LIBRARY READER\n''')
    def __init__(self, book_list, library_name):
        self.book_list = "list of books.txt"
        self.name = library_name
        self.book_dict = {}
        Id = 101
        with open(self.book_list) as b:
            content = b.readlines()
        for line in content:
            print(line)
print(Library("list of book.txt","Codewithme"))

