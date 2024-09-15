from flask import Flask
from flask_restx import Api


def create_app():
    app = Flask(__name__)

    api = Api(app=app)
    register_namespaces(api)
    initialize()
    return app


def register_namespaces(api: Api) -> None:
    from msg_api.hello.controller.hello import hello_ns

    ns_confs = [hello_ns]
    for ns_conf in ns_confs:
        api.add_namespace(ns_conf)


def initialize():
    pass
