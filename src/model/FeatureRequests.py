"""
Model class for the feature requests
"""
from sqlalchemy import UniqueConstraint

from src.model import db, DbModel

# Used by the clients and product_areas relationship, it is dynamically imported hence the look as though it's unused
from src.model import Clients, ProductAreas


clients = db.Table('client_to_feature_request',
                   db.Column('client_id', db.Integer, db.ForeignKey('clients.id'), primary_key=True),
                   db.Column('feature_request_id', db.Integer, db.ForeignKey('feature_requests.id'), primary_key=True),
                   db.Column('priority', db.Integer, index=True, comment="Priority is placed here as each client in a "
                                                                         "feature request feature must have a "
                                                                         "priority"),
                   UniqueConstraint('client_id', 'feature_request_id', name='client_feature_request_unique')
                   )

product_areas = db.Table('product_area_to_feature_request',
                         db.Column('product_area_id', db.Integer, db.ForeignKey('product_areas.id'), primary_key=True),
                         db.Column('feature_request_id', db.Integer, db.ForeignKey('feature_requests.id'),
                                   primary_key=True), UniqueConstraint('product_area_id', 'feature_request_id',
                                                                       name='product_area_feature_request_unique')
                         )


class FeatureRequests(DbModel):
    """
    Model class implementation
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.Text(), index=True, unique=True)
    # Client priority is placed in the clients and feature request relationship
    clients = db.relationship('Clients', secondary=clients, lazy='subquery',
                              backref=db.backref('feature_requests', lazy=True))
    target_date = db.Column(db.DateTime())
    product_areas = db.relationship('ProductAreas', secondary=product_areas, lazy='subquery',
                                    backref=db.backref('feature_requests', lazy=True))

    def __repr__(self):
        return '<{} {}>'.format(self.__table__, FeatureRequests.__dict__)


if __name__ == "__main__":
    print(FeatureRequests())
