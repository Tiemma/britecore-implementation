"""
Base class for importing model definitions
"""

from flask_sqlalchemy import SQLAlchemy

"""
Had to do a double declaration of app here because I couldn't import src.factory
I would refactor in the future, hopefully!

There's a cyclic dependency since create_api imports Users and this uses the db instance which calls AppFacory
and restarts the dependency loop, would fix at a later date

UPDATE: DB is instantiated from the AppFactory class in the src package
"""

db = SQLAlchemy()


class DbModel(db.Model):

    __abstract__ = True

    def __repr__(self):
        return '<{} {}>'.format(self.__table__, self.__dict__)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if 'password' not in c.name}


