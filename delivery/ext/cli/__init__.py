import click
from delivery.ext.db import db
from delivery.ext.auth.models import User
from delivery.ext.db import models

def init_app(app):
    @app.cli.command()
    def create_db():
        """Esse comando inicializa o db"""
        db.create_all()
