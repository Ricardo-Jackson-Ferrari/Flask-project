import click
import sqlalchemy
from delivery.ext.db import db
from delivery.ext.auth.models import User


@click.option('--name', '--n')
@click.option('--email', '--e')
@click.option('--password', '--p')
@click.option('--admin', '--a', is_flag=True, default=False)
def add_user(name, email, password, admin):
    """Esse comando adicionar um novo usuário"""
    try:
        user = User(
            name=name,
            email=email,
            password=password,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()
        click.echo('Usuário criado com sucesso!')
    except sqlalchemy.exc.IntegrityError:
        click.echo('Endereço de email já cadastrado!')
