"""
Base class for importing model definitions
"""
from sqlalchemy import UniqueConstraint

from src import db

clients = db.Table('client_to_feature_request',
                   db.Column('client_id', db.Integer, db.ForeignKey('client.id'), primary_key=True),
                   db.Column('feature_request_id', db.Integer, db.ForeignKey('feature_request.id'), primary_key=True),
                   db.Column('priority', db.Integer, index=True, comment="Priority is placed here as each client in a "
                                                                         "feature request feature must have a priority"),
                   UniqueConstraint('client_id', 'feature_request_id', name='client_feature_request_unique')
                   )

product_areas = db.Table('product_area_to_feature_request',
                         db.Column('product_area_id', db.Integer, db.ForeignKey('product_area.id'), primary_key=True),
                         db.Column('feature_request_id', db.Integer, db.ForeignKey('feature_request.id'), primary_key=True),
                         UniqueConstraint('product_area_id', 'feature_request_id', name='client_feature_request_unique')
                         )