from flask import render_template

from app import app
from models.order_list import order_list

@app.route('/order_list')
def index():
    return render_template('index.html', title = 'Nike', orders = order_list)
