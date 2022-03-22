import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash

from delivery.ext.auth import login_manager
from delivery.ext.auth.models import User
from delivery.ext.db import db


ALG = 'pbkdf2:sha256'


@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()


def create_user(name: str, email: str, password: str, admin: bool = False) -> User:
    user = User(
        name=name.strip.lower(),
        email=email.strip.lower(),
        password=generate_password_hash(password, ALG),
        admin=admin,
    )
    db.session.add(user)
    try:
        db.session.commit()
        return True
    except sqlalchemy.exc.IntegrityError:
        return False

def verify_user(email: str, password: str):
    user = db.session.query(User).filter(User.email == email.strip().lower()).first()
    if check_password_hash(user.password, password):
        return user
    else:
        return False
