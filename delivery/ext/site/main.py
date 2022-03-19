from operator import methodcaller
from flask import Blueprint, redirect, render_template, request, url_for

from delivery.ext.auth.form import UserForm
from delivery.ext.auth.controller import create_user


bp = Blueprint('site', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/about')
def about():
    return render_template('about.html')


@bp.route('/login')
def login():
    form = UserForm()
    return render_template('login.html', form=form)


@bp.route('/signup', methods=['POST', 'GET'])
def signup():
    form = UserForm()
    if form.validate_on_submit():
        res = create_user(email=form.email.data, password=form.password.data, name=form.name.data)
        if res:
            redirect('/login')

    # __import__('ipdb').set_trace()
    return render_template('userForm.html', form=form)
