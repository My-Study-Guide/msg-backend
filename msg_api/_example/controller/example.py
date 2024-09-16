from typing import List

from flask import make_response, request
from flask_restx import Namespace, Resource, fields

from common_lib.models.response import MsgBaseResponse
from msg_api._example.model.example import (
    MsgExamplePostRequest,
    MsgExampleUserInfo,
)
from msg_api._example.service.example import MsgExampleService

example_ns = Namespace("example", description="Example API")

example_request_model = example_ns.model(
    "ExampleRequest",
    {
        "name": fields.String(required=True, description="Your name"),
    },
)


@example_ns.route("/")
class MsgExampleController(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = MsgExampleService()

    def get(self):
        user_info: List[MsgExampleUserInfo] = self.service.get_user_info()
        response = make_response(
            MsgBaseResponse(data=user_info).to_dict(), 200
        )
        response.mimetype = "application/json"
        return response

    @example_ns.expect(example_request_model)
    def post(self):
        body = request.get_json(force=True, silent=True)
        query = MsgExamplePostRequest(**body)
        self.service.update_user_info(query)
        response = make_response(MsgBaseResponse(data=None).to_dict(), 201)

        response.mimetype = "application/json"
        return response
