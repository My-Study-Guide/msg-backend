from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from msg_api import config


def create_app():
    app = Flask(__name__)
    app.config.PROPAGATE_EXCEPTIONS = True
    app.config.from_object(config)

    api = Api(app=app)
    register_namespaces(api)
    CORS(app)
    initialize()
    return app


def register_namespaces(api: Api) -> None:
    from msg_api.hello.controller.hello import hello_ns

    ns_confs = [hello_ns]
    for ns_conf in ns_confs:
        api.add_namespace(ns_conf)


def initialize():
    pass
