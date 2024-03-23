from sqlalchemy import Column, Integer, String, Float, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import json

from __init__ import db, app


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    photo = Column(String(255))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():

        with open("data/categories.json", encoding="utf-8") as f:
            data = json.load(f)
            for p in data:
                cate = Category(**p)
                db.session.add(cate)
            db.session.commit()

        with open("data/products.json", encoding="utf-8") as f:
            prods = json.load(f)
            for p in prods:
                prod = Product(**p)
                db.session.add(prod)
            db.session.commit()
