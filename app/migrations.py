from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def make_migrations(db: SQLAlchemy, app: Flask):
    with app.app_context():
        db.drop_all()
        db.create_all()
