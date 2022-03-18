from flask import Blueprint, render_template, request

from delivery.ext.auth.form import UserForm


bp = Blueprint('site', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/about')
def about():
    return render_template('about.html')


@bp.route('/signup', methods=['POST', 'GET'])
def signup():
    form = UserForm()
    # __import__('ipdb').set_trace()
    return render_template('userForm.html', form=form)
