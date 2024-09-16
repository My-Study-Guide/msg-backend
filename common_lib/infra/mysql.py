import threading
from contextlib import contextmanager
from typing import Optional, Type

from mysql.connector.connection import MySQLConnection
from mysql.connector.pooling import MySQLConnectionPool

from common_lib.utils.singleton import Singleton, initialize_once


class DB(Singleton):
    @initialize_once
    def __init__(self, name: str):
        self.name = name
        self.db_user = None
        self.db_password = None
        self.db_name = None
        self.db_host = None
        self.db_port = 3306
        self.db_pool_size = 10
        self.db_connection_timeout = 20

        self._connection_pool = None
        self.__singleton_lock = threading.Lock()

    def init_app(
        self,
        db_user: str,
        db_password: str,
        db_name: str,
        db_host: str,
        db_port: int = 3306,
        db_pool_size: int = 10,
        db_connection_timeout: int = 20,
    ):
        self.db_user = db_user
        self.db_password = db_password
        self.db_name = db_name
        self.db_host = db_host
        self.db_port = db_port
        self.db_pool_size = db_pool_size
        self.db_connection_timeout = db_connection_timeout

        # 멀티 쓰레드에서 connection pool 이 여러번 초기화되는 거 방지
        # lock 을 획득한 thread 만 with 내부의 코드 실행 가능
        with self.__singleton_lock:
            if not self._connection_pool:
                self._connection_pool = MySQLConnectionPool(
                    host=self.db_host,
                    user=self.db_user,
                    password=self.db_password,
                    port=self.db_port,
                    db=self.db_name,
                    charset="utf8",
                    pool_name=f"{self.name}-pool",
                    pool_size=self.db_pool_size,
                    buffered=True,
                    connection_timeout=self.db_connection_timeout,
                )

    @contextmanager
    def cursor(
        self,
        buffered: Optional[bool] = None,
        raw: Optional[bool] = None,
        prepared: Optional[bool] = None,
        cursor_class: Optional[Type] = None,
        dictionary: Optional[bool] = None,
        named_tuple: Optional[bool] = None,
        pool: Optional[bool] = True,
    ) -> None:
        conn = (
            self._connection_pool.get_connection()
            if pool
            else MySQLConnection(
                host=self.db_host,
                user=self.db_user,
                password=self.db_password,
                db=self.db_name,
                port=self.db_port,
                charset="utf8",
                buffered=True,
                connection_timeout=self.db_connection_timeout,
            )
        )
        cursor = conn.cursor(
            buffered=buffered,
            raw=raw,
            prepared=prepared,
            cursor_class=cursor_class,
            dictionary=dictionary,
            named_tuple=named_tuple,
        )

        try:
            yield cursor
            conn.commit()
        except Exception as e:
            conn.rollback()  # transaction 이 실패할 경우 전체 롤백
            raise e
        finally:
            conn.close()
