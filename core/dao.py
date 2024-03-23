import json
from __init__ import app
from models import *


def get_Categories():
    return Category.query.all()


def get_Products(cate=None, kw=None,page=None):
    prods = Product.query

    if cate:
        prods = prods.filter(Product.category_id.__eq__(int(cate)))

    if kw:
        prods = prods.filter(Product.name.contains(kw))

    if page:
        page_size = app.config["page_size"]
        start = (int(page) - 1) * page_size
        prods = prods.slice(start, start + page_size)

    return prods.all()


def count_products():
    return Product.query.count()


def get_product_by_id(id=None):
    return Product.query.get(id)
