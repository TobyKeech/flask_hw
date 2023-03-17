from flask import *

from app import app
from models.book_list import *
from models.book import *

@app.route('/books')
def index():
    return render_template('index.html', 
                           title = 'CodeClan Libary', 
                           books_in_store = book_list)

@app.route('/books/<id>')
def order(id):
    return render_template('order.html', 
                           title = 'CodeClan Libary', 
                           solo_book = book_list[int(id)])

@app.route('/books', method = ['POST'])
def add_new_book():
    book_title = request.form['title']
    book_author = request.form['author'] 
    book_genre = request.form['genre']

    new_book = Book(book_title, book_author, book_genre)

    add_new_book(new_book)

    return redirect ('/books')
        
