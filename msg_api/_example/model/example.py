from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin


@dataclass
class MsgExamplePostRequest(DataClassJsonMixin):
    name: str


@dataclass
class MsgExampleUserInfo(DataClassJsonMixin):
    id: str
    name: str
    created_at: str
