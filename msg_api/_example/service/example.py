from typing import List

from msg_api._example.dao.example import MsgExampleDAO
from msg_api._example.model.example import (
    MsgExamplePostRequest,
    MsgExampleUserInfo,
)


class MsgExampleService:
    def __init__(self):
        self.dao = MsgExampleDAO()

    def get_user_info(self) -> List[MsgExampleUserInfo]:
        return self.dao.get_user_info()

    def update_user_info(self, query: MsgExamplePostRequest):
        self.dao.save_user_info(query)
