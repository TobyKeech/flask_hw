from models.book import *

book1 = Book ("To Kill a Mockingbird", "Harper Lee", "Ethics",True)
book2 = Book ("Bourne Identity", "Robert Ludlum", "Thriller", False)
book3 = Book ("Catcher in the Rye", "J D Salinger", "Coming of Age ", True)

book_list = [book1, book2, book3]


def add_new_book(book):
    book_list.append(book)

def delete_book(index):
    book = book_list[index]
    book_list.remove(book) 