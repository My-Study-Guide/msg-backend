from flask import make_response, request
from flask_restx import Namespace, Resource, fields

from common_lib.models.response import MsgBaseResponse
from msg_api.analyze.model.analyze import (
    MsgAnalyzePostRequest,
    MsgAnalyzePostResponse,
)
from msg_api.analyze.service.analyze import MsgAnalyzeService

analyze_ns = Namespace("analyze", description="Analyze API")

analyze_request_model = analyze_ns.model(
    "ExampleRequest",
    {
        "topic": fields.String(required=True, description="topic"),
        "urls": fields.List(
            required=True,
            description="list of urls",
            cls_or_instance=fields.String,
        ),
    },
)

result_model = analyze_ns.model(
    "result",
    {
        "url": fields.String(description="페이지 URL"),
        "status": fields.String(description="url 안열리면 error, 열리면 success"),
        "score": fields.Float(description="집중도"),
        "summary": fields.String(description="url의 주제"),
    },
)


@analyze_ns.route("/")
class MsgAnalyzeController(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = MsgAnalyzeService()

    @analyze_ns.expect(analyze_request_model)
    def post(self):
        body = request.get_json(force=True, silent=True)
        query = MsgAnalyzePostRequest(**body)
        results: MsgAnalyzePostResponse = self.service.analyze_urls(
            topic=query.topic, urls=query.urls
        )
        response = make_response(MsgBaseResponse(data=results).to_dict(), 200)

        response.mimetype = "application/json"
        return response
