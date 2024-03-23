from flask_admin import Admin, expose, BaseView
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


class Stats(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')


admin.add_view(CategoryModelView(Category, db.session))
admin.add_view(ProductModelView(Product, db.session))
admin.add_view(Stats(name="Thong ke"))
