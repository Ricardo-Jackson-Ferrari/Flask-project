from flask_admin.contrib.sqla import ModelView


def format_user(self, request, user, *args):
    return user.email.upper()

class UserAdmin(ModelView):
    """Admin interface"""
    column_formatters = {'email': format_user}