from app.urlink import db


class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.String, primary_key=True)
    authorities = db.Column(db.JSON)

    def __init__(self, id, authorities):
        self.id = id
        self.authorities = authorities
