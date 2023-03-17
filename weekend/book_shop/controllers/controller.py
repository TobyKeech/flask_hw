from flask import *

from app import app
from models.book_list import *
from models.book import *


@app.route('/books')
def home():
    return render_template('base.html',
                           title = 'CodeClan Libary')

@app.route('/books/list')
def index():
    return render_template('index.html', 
                           title = 'CodeClan Libary', 
                           books_in_store = book_list)


@app.route('/books/<id>')
def order(id):
    return render_template('order.html', 
                           title = 'CodeClan Libary', 
                           solo_book = book_list[int(id)])

@app.route('/books/list', methods = ['POST'])

def add_book():
    book_title = request.form['title']
    book_author = request.form['author'] 
    book_genre = request.form['genre']

    new_book = Book(book_title, book_author, book_genre)

    add_new_book(new_book)

    return redirect ('/books/list')


@app.route('/books/list', methods = ['DELETE'])

def delete_book():
    book_title = request.form['title']
    book_author = request.form['author'] 
    book_genre = request.form['genre']

    book_to_delete = Book(book_title, book_author, book_genre)

    delete_book(book_to_delete)

    return redirect ('books/list')



        
