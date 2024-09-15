from flask import jsonify, request, make_response
from flask_restx import Resource, Namespace

hello_ns = Namespace('hello', description='Hello API')


@hello_ns.route("/")
class HelloController(Resource):
    def get(self):
        """
            Test hello get
        """

        return make_response(jsonify({"status": "ok", "data": None}, 200))

    def post(self):
        """
            Test hello post
        """
        body = request.get_json(force=True, silent=True)
        return make_response(jsonify({"status": "ok", "data": body}, 201))

    def put(self):
        """
            Test hello put
        """
        return make_response(jsonify({"status": "ok", "data": None}), 200)

    def patch(self):
        """
            Test hello patch
        """
        return make_response(jsonify({"status": "ok", "data": None}), 200)
