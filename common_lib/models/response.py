from dataclasses import dataclass
from typing import Any, Optional

from dataclasses_json import DataClassJsonMixin


@dataclass
class MsgBaseResponse(DataClassJsonMixin):
    data: Optional[Any]


@dataclass
class MsgError(DataClassJsonMixin):
    message: str


@dataclass
class MsgErrorResponse(MsgBaseResponse):
    error: MsgError
