import string

from app.urlink import db
from handling.utils.generators import random_string
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

    @staticmethod
    def __generate_random_string():
        formatted = random_string()

        while Link.exists_by_formatted(formatted):
            formatted = random_string()

        return formatted

    @staticmethod
    def create(owner_id, original, title, base_url):

        key = Link.__generate_random_string()
        formatted = base_url + 'ref/' + key

        link = Link(
            title,
            original,
            formatted,
            key,
            owner_id=owner_id
        )
        db.session.add(link)
        db.session.commit()

        return formatted

    @staticmethod
    def get_by_key(key):
        return Link.query.filter_by(key=key).first()

    @staticmethod
    def exists_by_formatted(formatted):
        return Link.get_by_key(formatted) is not None

    @staticmethod
    def get_all_by_owner(owner_id):
        return Link.query.filter_by(owner=owner_id).all()
