import wtforms as wtf
from flask_wtf import FlaskForm


class UserFormRegister(FlaskForm):
    name = wtf.StringField('Nome')
    email = wtf.EmailField('Email', [wtf.validators.DataRequired(), wtf.validators.Email()])
    password = wtf.PasswordField('Senha', [wtf.validators.DataRequired()])


class UserFormLogin(FlaskForm):
    email = wtf.EmailField('Email', [wtf.validators.DataRequired(), wtf.validators.Email()])
    password = wtf.PasswordField('Senha', [wtf.validators.DataRequired()])
