from flask import *

from app import app
from models.book_list import book_list

@app.route('/orders')
def index():
    return render_template('index.html', 
                           title = 'Waterstones', 
                           books_in_store = book_list)

@app.route('/orders/<id>')
def order(id):
    return render_template('order.html', 
                           title = 'Waterstones', 
                           solo_book = book_list[int(id)])