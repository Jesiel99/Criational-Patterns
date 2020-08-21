import json
import xmltodict


class Connection:

    __connection = None

    def __new__(cls, user=None, password=None, host=None, port=None):
        cls.user = user
        cls.password = password
        cls.host = host
        cls.port = port
        if cls.__connection is None:
            cls.__connection = super().__new__(cls)
        return cls.__connection

    @staticmethod
    def json(data):
        data = json.loads(data)
        Connection.set(data['user'], data['password'], data['host'], data['port'])
        return Connection.__connection

    @staticmethod
    def xml(where_it_is, data):
        data = xmltodict.parse(data)
        data = data[where_it_is]
        Connection.set(data['user'], data['password'], data['host'], data['port'])
        return Connection.__connection

    @staticmethod
    def set(user, password, host, port):
        Connection.__connection.user = user
        Connection.__connection.password = password
        Connection.__connection.host = host
        Connection.__connection.port = port

