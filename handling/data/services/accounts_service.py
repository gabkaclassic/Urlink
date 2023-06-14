from handling.data.entities.accounts import Account
from app.urlink import db


def create_user(id):
    account = Account(id, ['USER'])
    db.session.add(account)
    db.session.commit()


def exists_by_id(id):
    return get_by_id(id) is not None


def get_by_id(id):
    return Account.query.filter_by(id=id).first()
