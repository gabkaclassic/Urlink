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