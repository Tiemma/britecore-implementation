"""
Model class for the user
"""
from src import db


class User(db.Model):
    """
    Model class implementation
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    # Leaving this a string as a UUID / hash of the username would be easy to manage
    iws_employee_id = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(User.__dict__)


if __name__  == "__main__":
    print(User())