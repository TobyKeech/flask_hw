from models.book import *

book1 = Book ("To Kill a Mockingbird", "Harper Lee", "Ethics")
book2 = Book ("Bourne Identity", "Robert Ludlum", "Thriller")
book3 = Book ("Catcher in the Rye", "J D Salinger", "Coming of Age ")

book_list = [book1, book2, book3]


def add_new_book(book):
    book_list.append(book)

def delete_book(book):
    book_list.remove(book)