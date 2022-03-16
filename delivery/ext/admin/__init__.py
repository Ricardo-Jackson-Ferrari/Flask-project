from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from delivery.ext.db import db
from delivery.ext.admin.menus import StoreUser
from delivery.ext.db.models import Store, Order, Address, Category


admin = Admin()


def init_app(app):
    admin.name = 'delivery'
    admin.template_mode = 'bootstrap4'
    admin.init_app(app)

    admin.add_view(StoreUser(Store, db.session))
    admin.add_view(ModelView(Category, db.session))
    admin.add_view(ModelView(Order, db.session))
    admin.add_view(ModelView(Address, db.session))