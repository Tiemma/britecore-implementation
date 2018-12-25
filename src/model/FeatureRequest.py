"""
Model class for the feature requests
"""
from src import db
from src.model import clients, product_areas

# Used by the clients and product_areas relationship, it is dynamically imported hence the look as though it's unused
from src.model import Client, ProductArea


class FeatureRequest(db.Model):
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
        return '<FeatureRequest {}>'.format(FeatureRequest.__dict__)


if __name__ == "__main__":
    print(FeatureRequest())