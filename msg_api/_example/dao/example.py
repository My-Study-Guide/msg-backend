from typing import List

from common_lib.infra.mysql import DB
from msg_api._example.model.example import (
    MsgExamplePostRequest,
    MsgExampleUserInfo,
)


class MsgExampleDAO:
    def __init__(self):
        self.db = DB()

    def save_user_info(self, query: MsgExamplePostRequest) -> None:
        with self.db.cursor(dictionary=True) as cursor:
            sql = """
                INSERT INTO TEST(
                    NAME
                )
                VALUES (
                    %(name)s
                )
            """
            data = {"name": query.name}
            cursor.execute(sql, data)

    def get_user_info(self) -> List[MsgExampleUserInfo]:
        with self.db.cursor(dictionary=True) as cursor:
            results = []
            sql = """
                SELECT
                  ID,
                  NAME,
                  CREATED_AT
                FROM
                  TEST
            """
            cursor.execute(sql)
            rows = cursor.fetchall()

            for row in rows:
                results.append(
                    MsgExampleUserInfo(
                        id=row["ID"],
                        name=row["NAME"],
                        created_at=row["CREATED_AT"].isoformat(),
                    )
                )

            return results
