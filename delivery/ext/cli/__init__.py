import click
from delivery.ext.db import db
from delivery.ext.site import models #noqa

def init_app(app):
    @app.cli.command()
    def create_db():
        """Esse comando inicializa o db"""
        db.create_all()

    @app.cli.command()
    @click.option('--email', '--e')
    @click.option('--password', '--p')
    @click.option('--admin', '--a', is_flag=True, default=False)
    def add_user(email, password, admin):
        """Esse comando adicionar um novo usuário"""
        user = models.User(
            email=email,
            password=password,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()
        click.echo('Usuário criado com sucesso!')