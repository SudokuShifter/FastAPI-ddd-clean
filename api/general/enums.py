from enum import Enum


class SomeEnum:
    ONE = 1
    TWO = 2


class RoutersMetainfo(Enum):
    DEFAULT_TAGS: list[str] = ["default"]
    DEFAULT_PREFIX: str = "/api/v1"
