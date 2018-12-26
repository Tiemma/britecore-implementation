"""
Model class for the product area
"""
from src.model import db, DbModel


class ProductArea(DbModel):
    """
    Model class implementation
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<{} {}>'.format(self.__table__, self.__dict__)


if __name__ == "__main__":
    print(ProductArea())
