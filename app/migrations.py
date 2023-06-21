from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def make_migrations(db: SQLAlchemy, app: Flask):
    from handling.data.entities.accounts import Account
    from handling.data.entities.visits import Visit
    from handling.data.entities.links import Link
    with app.app_context():
        db.create_all()
