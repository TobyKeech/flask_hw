from flask import *
from app import app
from models.book_list import *
from models.book import *


@app.route('/')
def home():
    return render_template('base.html',
                           title = 'CodeClan Libary')

@app.route('/books')
def books_list():
    return render_template('index.html', 
                           title = 'CodeClan Libary', 
                           books_in_store = book_list)

@app.route('/books/<index>')
def book_show(index):
    return render_template('order.html', 
                           title = 'CodeClan Libary', 
                           solo_book = book_list[int(index)])
@app.route('/books/new')
def book_new():
    return render_template('new.html', 
                           title = 'CodeClan Libary', 
                           books_in_store = book_list)

@app.route('/books/new', methods = ['POST'])
def add_book():
    book_title = request.form['title']
    book_author = request.form['author'] 
    book_genre = request.form['genre']
    new_book = Book(book_title, book_author, book_genre, True)
    add_new_book(new_book)
    return redirect ('/books')


@app.route('/books/delete/<index>', methods=['POST'])
def books_delete(index):
    delete_book(int(index))
    return redirect('/books')

