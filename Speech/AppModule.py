from injector import Module, singleton
from flask import Flask


class AppModule(Module):
    _flask_app = None
    _instance = None

    def __init__(self):
        raise Exception('call instance()')

    @classmethod
    def _new_instance(cls):
        cls._instance = cls.__new__(cls)
        cls._flask_app = Flask(__name__)

    @classmethod
    def flask_app(cls):
        if cls._flask_app is None:
            cls._new_instance()
        return cls._flask_app

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._new_instance()
        return cls._instance

    def configure(self, binder):
        pass
