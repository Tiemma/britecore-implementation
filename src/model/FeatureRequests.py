"""
Model class for the feature requests
"""
from src.model import clients, db, product_areas, DbModel

# Used by the clients and product_areas relationship, it is dynamically imported hence the look as though it's unused
from src.model import Client, ProductArea


class FeatureRequest(DbModel):
    """
    Model class implementation
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.Text(), index=True, unique=True)
    # Client priority is placed in the clients and feature request relationship
    clients = db.relationship('Client', secondary=clients, lazy='subquery',
                              backref=db.backref('feature_requests', lazy=True))
    target_date = db.Column(db.DateTime())
    product_areas = db.relationship('ProductArea', secondary=product_areas, lazy='subquery',
                                    backref=db.backref('feature_requests', lazy=True))

    def __repr__(self):
        return '<{} {}>'.format(self.__table__, FeatureRequest.__dict__)


if __name__ == "__main__":
    print(FeatureRequest())
