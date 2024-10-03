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
    from msg_api._example.controller.example import example_ns
    from msg_api.analyze.controller.analyze import analyze_ns

    ns_confs = [hello_ns, example_ns, analyze_ns]
    for ns_conf in ns_confs:
        api.add_namespace(ns_conf)


def initialize():
    pass
    # db = DB()
    # db.init_app(
    #     db_host=config.MYSQL_HOST,
    #     db_user=config.MYSQL_USER,
    #     db_password=config.MYSQL_PASSWORD,
    #     db_port=config.MYSQL_PORT,
    #     db_name=config.MYSQL_DB,
    #     db_pool_size=config.MYSQL_POOL_SIZE,
    #     db_connection_timeout=config.MYSQL_CONNECTION_TIMEOUT,
    # )
