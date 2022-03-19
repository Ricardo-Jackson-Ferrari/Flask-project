from flask import flash
from flask_admin.actions import action
from flask_admin.contrib.sqla import ModelView, fields
from flask_admin.form.fields import Select2Field
from sqlalchemy.orm import load_only

from delivery.ext.auth.models import User
from delivery.ext.db import db
from delivery.ext.db.models import Store


class StoreUser(ModelView):
    """Admin interface"""
    column_list = ('name', 'user', 'active', 'create')
    form_columns = ('name', 'user', 'active', 'create')

    column_searchable_list = ['name']
    column_filters = ['user']
    
    #with_entities
    # column_hide_backrefs = False
    # form_extra_fields = {
    #     'user': fields.QuerySelectField(
    #         label='Usuario',
    #         query_factory=lambda: User.query.all()
    #         # query_factory=lambda: db.session.query(User.name).all()
    #     )
    # }

    can_delete = True
    can_create = True
    can_edit = False
