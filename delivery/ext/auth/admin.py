from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from delivery.ext.db import db
from delivery.ext.auth.models import User
from flask import flash

def format_user(self, request, user, *args):
    # return user.email
    return user.email.replace(user.email[user.email.rindex('@'):], '*'*len(user.email[user.email.rindex('@'):]))

class UserAdmin(ModelView):
    """Admin interface"""
    column_formatters = {'email': format_user}
    column_list = ('name', 'email', 'admin')
    form_columns = ('name', 'email', 'password', 'admin')

    column_searchable_list = ['email']
    column_filters = ['admin']
    
    can_delete = True
    can_create = True
    can_edit = False


    @action(
        'toggle_admin',
        'Toggle admin status',
        'Are you sure ?'
    )
    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
        db.session.commit()
        flash(f'{len(users)} usuários alterados com sucesso!', 'success')


    @action(
        'send_email',
        'Send email for user',
        'Are you sure ?'
    )
    def send_email(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        
        flash(f'{len(users)} emails enviados!', 'success')
