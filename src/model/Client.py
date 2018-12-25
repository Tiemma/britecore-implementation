"""
Model class for the client
"""
from src import db


class Client(db.Model):
    """
    Model class implementation
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    address = db.Column(db.Text())

    def __repr__(self):
        return '<Client {}>'.format(Client.__dict__)


if __name__  == "__main__":
    print(Client())