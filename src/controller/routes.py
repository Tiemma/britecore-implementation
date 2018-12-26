"""
Controller functions for handling route related functions
"""
from typing import Dict


class ResponseBody:
    """
    Response body definition to enforce API response schema across all definitions
    """
    __message = None
    __data = dict()
    __status = None

    def __init__(self, data: Dict, message: str, status: int, **kwargs):
        if data is None:
            raise NotImplementedError("Data must not be null in response body")

        if message is None:
            raise NotImplementedError("Message must not be null in response body")

        if status is None:
            raise NotImplementedError("Status must not be null in response body")

        self.data = data
        self.data.update(kwargs)
        self.message = message
        self.status = status

    @property
    def body(self):
        return {'data': self.data, 'message': self.message, 'status': self.status}, self.status

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message):
        self.__message = message

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status






