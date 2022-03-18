from ctypes import sizeof
import wtforms as wtf
from flask_wtf import FlaskForm


class UserForm(FlaskForm):
    name = wtf.StringField('Nome')
    email = wtf.EmailField('Email', [wtf.validators.DataRequired(), wtf.validators.Email()])
    password = wtf.PasswordField('Senha', [wtf.validators.DataRequired()])
