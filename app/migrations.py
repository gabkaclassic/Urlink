from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func


def make_migrations(db: SQLAlchemy, app: Flask):
    from handling.data.models import Account, Link, Visit

    with app.app_context():
        # db.drop_all()
        db.create_all()
        acc = Account('641da429e97f324462a6eac2', {})
        link = Link(acc, 'original', 'formatted')
        visit = Visit(link, {"country": "RU", "region": "Moscow", "city": "Zelenograd"})
        db.session.add(acc)
        db.session.add(link)
        db.session.add(visit)
        db.session.commit()
        print(Account.count())
