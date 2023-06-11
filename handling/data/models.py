from app.urlink import db
import datetime

class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.String, primary_key=True)
    authorities = db.Column(db.JSON)

    def __init__(self, id, authorities):
        self.id = id
        self.authorities = authorities

    @staticmethod
    def create_user(id):
        account = Account(id, ['USER'])
        db.session.add(account)
        db.session.commit()

    @staticmethod
    def exists_by_id(id):
        return Account.query.filter_by(id=id).first() is not None

class Link(db.Model):
    __tablename__ = 'links'
    owner = db.Column(db.String, db.ForeignKey(Account.id), primary_key=True)
    original = db.Column(db.String, nullable=False, primary_key=True)
    formatted = db.Column(db.String, nullable=False, unique=True, primary_key=True)

    __table_args__ = (db.UniqueConstraint('owner', 'original', name='owner_original_uk'),)

    def __init__(self, owner, original, formatted):
        self.owner = owner.id
        self.original = original
        self.formatted = formatted


class Visit(db.Model):
    __tablename__ = 'visits'
    id = db.Column(db.Integer, primary_key=True)
    visited_link = db.Column(db.String, db.ForeignKey(Link.formatted, ondelete='CASCADE'), nullable=False)
    location = db.Column(db.JSON)
    time = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, visited, location):
        self.visited_link = visited.formatted
        self.location = location
        self.time = datetime.datetime.now()


