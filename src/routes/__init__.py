"""
Declaration of API definitions for flask restplus
"""
from flask_restplus import Api
from src.routes.Auth import AUTH_NS


def create_api():
    api = Api(title="Stack Overflow Lite",
              description="""
              This is where the rest endpoints for the application is defined.
              Multiple namespaces have been placed here for ease of reach
              """,
              prefix="/api/v1",
              contact="Bakare Emmanuel",
              contact_email="emmanueltimmy98@gmail.com",
              version="1.0")

    api.add_namespace(AUTH_NS, path="/auth")

    return api

