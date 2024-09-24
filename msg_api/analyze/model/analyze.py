from dataclasses import dataclass
from typing import List

from dataclasses_json import DataClassJsonMixin


@dataclass
class MsgAnalyzePostRequest(DataClassJsonMixin):
    topic: str
    urls: List[str]


@dataclass
class UrlInfo(DataClassJsonMixin):
    url: str
    status: str
    score: float
    summary: str


@dataclass
class MsgAnalyzePostResponse(DataClassJsonMixin):
    results: List[UrlInfo]
