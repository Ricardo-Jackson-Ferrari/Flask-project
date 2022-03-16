from delivery.ext.db import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column("email", db.Unicode, unique=True)
    password = db.Column("password", db.Unicode)
    admin = db.Column("admin", db.Boolean)
    name = db.Column("name", db.Unicode)

    def __repr__(self):
        return f'[id]: {self.id} [user]: {self.name.title()}'