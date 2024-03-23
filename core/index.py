import math

from flask import render_template, request, redirect
from core import dao
from __init__ import app
from admin import admin

@app.route("/")
def index():
    cate = request.args.get('category_id')
    kw = request.args.get('q')
    page = request.args.get('page')

    prod = dao.get_Products(cate=cate, kw=kw, page=page)
    pages = math.ceil(dao.count_products() / app.config['page_size'])
    return render_template('index.html', prod=prod, pages = int(pages))


@app.route("/products/<int:id>")
def product(id):
    product = dao.get_product_by_id(id=id)
    return render_template('product-detail.html', product=product)


@app.context_processor
def common_attributes():
    return {
        'categories': dao.get_Categories()
    }


@app.route('/login', methods=['get', 'post'])
def login_my_user():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        if username.__eq__('admin') and password.__eq__('123'):
            return redirect('/')

    return render_template('login.html')


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
