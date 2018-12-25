"""
Model class for the product area
"""
from src import db


class ProductArea(db.Model):
    """
    Model class implementation
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(ProductArea.__dict__)


if __name__ == "__main__":
    print(ProductArea())