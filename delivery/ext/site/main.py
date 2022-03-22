from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_user, logout_user

from delivery.ext.auth.form import UserFormRegister, UserFormLogin
from delivery.ext.auth.controller import create_user, verify_user


bp = Blueprint('site', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/about')
def about():
    return render_template('about.html')


@bp.route('/signup', methods=['POST', 'GET'])
def signup():
    form = UserFormRegister()
    if form.validate_on_submit():
        res = create_user(email=form.email.data, password=form.password.data, name=form.name.data)
        if res:
            return redirect(url_for('site.login'))

    return render_template('register.html', form=form)


@bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email, password = (request.form['email'], request.form['password'])
        user = verify_user(email=email, password=password)
        if not user:
            return redirect(url_for('site.login'))
        
        login_user(user)
        return redirect(url_for('site.index'))
    form = UserFormLogin()
    return render_template('login.html', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('site.login'))
