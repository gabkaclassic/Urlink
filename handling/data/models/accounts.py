from app.urlink import db


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
        return Account.get_by_id(id) is not None

    @staticmethod
    def get_by_id(id):
        return Account.query.filter_by(id=id).first()
