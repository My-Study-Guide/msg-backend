from os.path import dirname, join

from dotenv import load_dotenv

from common_lib.utils.env_loader import load_env

dotenv_path = join(dirname(__file__), "../", ".env")
load_dotenv(dotenv_path)

MYSQL_HOST = load_env("MYSQL_HOST", required=True)
MYSQL_PORT = load_env("MYSQL_PORT", "3306", as_type=int)
MYSQL_PASSWORD = load_env("MYSQL_PASSWORD", required=True)
MYSQL_DB = load_env("MYSQL_DB", required=True)
MYSQL_USER = load_env("MYSQL_USER", required=True)
MYSQL_POOL_SIZE = load_env("MYSQL_POOL_SIZE", "10", as_type=int)
MYSQL_CONNECTION_TIMEOUT = load_env(
    "MYSQL_CONNECTION_TIMEOUT", "20", as_type=int
)
MODEL_URL = load_env("MODEL_URL", required=True)
