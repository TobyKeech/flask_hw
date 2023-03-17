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