import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash

from delivery.ext.auth.models import User
from delivery.ext.db import db


ALG = 'pbkdf2:sha256'


def create_user(name: str, email: str, password: str, admin: bool = False) -> User:
    user = User(
        name=name,
        email=email,
        password=generate_password_hash(password, ALG),
        admin=admin,
    )
    db.session.add(user)
    try:
        db.session.commit()
        return True
    except sqlalchemy.exc.IntegrityError:
        return False
