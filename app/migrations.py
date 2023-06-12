from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import asyncio
def make_migrations(db: SQLAlchemy, app: Flask):
    from handling.data.models.links import Link
    from handling.data.models.visits import Visit
    from handling.data.models.accounts import Account

    with app.app_context():
        pass
        # db.drop_all()
        # db.create_all()
        # acc = Account('641da429e97f324462a6eac2', {})
        # link = Link('title', 'original', 'formatted', owner=acc)
        # visit = Visit(link, {"country": "RU", "region": "Moscow", "city": "Zelenograd"})
        # db.session.add(acc)
        # db.session.add(link)
        # db.session.add(visit)
        # db.session.commit()
        # statisttics = asyncio.run(Visit.statistics(link))
        # print(statisttics)
