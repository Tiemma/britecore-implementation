"""
Model class for the client
"""
from src.model import db, DbModel


class Clients(DbModel):
    """
    Model class implementation
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    address = db.Column(db.Text())

    def __repr__(self):
        return '<{} {}>'.format(self.__table__, self.__dict__)


if __name__ == "__main__":
    print(Clients())
