from flask import render_template

from app import app
from models.order_list import order_list

@app.route('/orders')
def index():
    return render_template('index.html', 
                           title = 'Nike', 
                           orders = order_list)

@app.route('/orders/<id>')
def order(id):
    return render_template('order.html', 
                           title = 'Nike', 
                           my_order = order_list[int(id)])
