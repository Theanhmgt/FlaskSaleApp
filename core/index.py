from flask import Flask, render_template, request

from core import dao

name = "Sale app"
app = Flask(name)


@app.route("/")
def index():
    cate = request.args.get('cate_id')
    kw = request.args.get('q')

    categories = dao.get_Categories()
    prod = dao.get_Products(cate, kw)
    return render_template('index.html', categories=categories, prod=prod)


@app.route("/products/<int:id>")
def product(id):
    product = dao.get_product_by_id(id=id)
    return render_template('product-detail.html', product=product)


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
