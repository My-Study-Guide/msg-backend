from functools import wraps
from typing import Callable, TypeVar


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


R = TypeVar("R")


def initialize_once(init_method: Callable[..., R]) -> Callable[..., R]:
    @wraps(init_method)
    def impl(self, name: str = "default", *args, **kwargs):
        initialized = getattr(self, "__initialized", False)
        if initialized:
            return
        else:
            self.__initialized = True
            return init_method(self, name, *args, **kwargs)

    return impl
