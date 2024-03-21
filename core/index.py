from flask import Flask, render_template, request

from core import dao

name = "Sale app"
app = Flask(name)


@app.route("/")
def index():
    cate = request.args.get('cate_id')
    kw = request.args.get('q')

    prod = dao.get_Products(cate, kw)
    return render_template('index.html',  prod=prod)


@app.route("/products/<int:id>")
def product(id):
    product = dao.get_product_by_id(id=id)
    return render_template('product-detail.html', product=product)


@app.context_processor
def common_attributes():
    return {
        'categories': dao.get_Categories()
    }


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
