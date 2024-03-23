from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import *
from __init__ import app, db

admin = Admin(app, name="Quan ly ban hang", template_mode="bootstrap4")


class CategoryModelView(ModelView):
    column_list = ['id', 'name', 'products']


class ProductModelView(ModelView):
    column_list = ['id', 'name', 'price', 'category_id']
    column_searchable_list = ['name', 'price', 'category_id']
    column_filters = ['category_id', 'name', 'price']
    can_export = True


admin.add_view(CategoryModelView(Category, db.session))
admin.add_view(ProductModelView(Product, db.session))
