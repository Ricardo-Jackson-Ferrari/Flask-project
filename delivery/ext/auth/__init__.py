from flask_login import LoginManager

from delivery.ext.auth import models
from delivery.ext.auth.commands import add_user
from delivery.ext.db import db
from delivery.ext.auth.admin import UserAdmin
from delivery.ext.admin import admin
from delivery.ext.auth.models import User

login_manager = LoginManager()

def init_app(app):
    """TODO: Inicializar Flask Simple Login + JWT"""
    login_manager.init_app(app)
    app.cli.command()(add_user)
    admin.add_view(UserAdmin(User, db.session))
