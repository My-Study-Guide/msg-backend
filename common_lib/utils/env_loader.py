import os
from distutils.util import strtobool
from typing import Optional, Type


class MissingRequiredEnvironmentVariable(Exception):
    def __init__(self, env_name: str):
        _message = f"Missing Required Environment Variable '{env_name}'"
        Exception.__init__(self, _message)
        self.message = _message
        self.env_name = env_name


def load_env(env_name: str, default: Optional[str] = None, required: bool = False, as_type: Optional[Type] = None) -> \
        Optional[any]:
    if not isinstance(default, (str, type(None))):
        raise TypeError(f"type of default allowed only str (current: {type(default)})")

    env_val = os.environ.get(env_name, default)
    if required is True and env_val is None:
        raise MissingRequiredEnvironmentVariable(env_name)

    if as_type and env_val:
        try:
            if as_type is bool:
                return bool(strtobool(env_val))
            return as_type(env_val)
        except (ValueError, TypeError):
            raise ValueError(f"Cannot cast environment variable '{env_name}' to {as_type.__name__}")

    return env_val
