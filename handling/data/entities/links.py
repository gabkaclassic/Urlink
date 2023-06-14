import string

from app.urlink import db
from .accounts import Account


class Link(db.Model):
    __tablename__ = 'links'
    owner = db.Column(db.String, db.ForeignKey(Account.id), primary_key=True)
    original = db.Column(db.String, nullable=False, primary_key=True)
    formatted = db.Column(db.String, nullable=False, unique=True)
    key = db.Column(db.String, nullable=False, unique=True)
    title = db.Column(db.String, nullable=False)

    __table_args__ = (db.UniqueConstraint('owner', 'original', 'title', name='owner_original_title_uk'),)

    CHARACTERS = string.ascii_letters + string.digits + string.punctuation

    def __init__(self, title, original, formatted, key, owner=None, owner_id=None):
        self.owner = owner.id if owner_id is None else owner_id
        self.original = original
        self.key = key
        self.formatted = formatted
        self.title = title
