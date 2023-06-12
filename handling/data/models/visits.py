from app.urlink import db
import datetime
from .links import Link
from sqlalchemy import func


class Visit(db.Model):
    __tablename__ = 'visits'
    id = db.Column(db.Integer, primary_key=True)
    visited_link = db.Column(db.String, db.ForeignKey(Link.formatted, ondelete='CASCADE'), nullable=False)
    country = db.Column(db.String)
    region = db.Column(db.String)
    city = db.Column(db.String)
    time = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, visited, location):
        self.visited_link = visited.formatted
        self.country = location['country']
        self.city = location['city']
        self.region = location['region']
        self.time = datetime.datetime.now()

    @staticmethod
    async def create(link: Link, location):
        visit = Visit(link, location)
        db.session.add(visit)
        db.session.commit()

    @staticmethod
    async def statistics_by(link, by):
        return db.session.query(by, func.count(1)) \
            .filter_by(visited_link=link.formatted) \
            .group_by(by) \
            .all()

    @staticmethod
    async def statistics(link):
        return [
            await Visit.statistics_by(link, Visit.country),
            await Visit.statistics_by(link, Visit.region),
            await Visit.statistics_by(link, Visit.city),
        ]