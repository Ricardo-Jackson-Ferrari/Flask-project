from flask_admin.contrib.sqla import ModelView


def format_user(self, request, user, *args):
    # return user.email
    return user.email.replace(user.email[user.email.rindex('@'):], '*'*len(user.email[user.email.rindex('@'):]))

class UserAdmin(ModelView):
    """Admin interface"""
    column_formatters = {'email': format_user}
    column_list = ('name', 'email', 'admin')
    form_columns = ('name', 'email', 'password', 'admin')
    