from flask import flash
from flask_admin.contrib.sqla import ModelView, fields

from delivery.ext.auth.models import User
from delivery.ext.db import db


class StoreUser(ModelView):
    """Admin interface"""
    column_list = ('name', 'user', 'active', 'create')
    form_columns = ('name', 'user', 'active', 'create')

    column_searchable_list = ['name']
    column_filters = ['user']

    can_delete = True
    can_create = True
    can_edit = False
