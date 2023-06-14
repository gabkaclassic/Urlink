from sqlalchemy import func

from handling.data.entities.links import Link
from handling.data.entities.visits import Visit
from app.urlink import db

async def create(link: Link, location):
    visit = Visit(link, location)
    db.session.add(visit)
    db.session.commit()


async def statistics_by(link, by):
    return db.session.query(by, func.count(1)) \
        .filter_by(visited_link=link.formatted) \
        .group_by(by) \
        .all()


async def statistics(link):
    return [
        await statistics_by(link, Visit.country),
        await statistics_by(link, Visit.region),
        await statistics_by(link, Visit.city),
    ]