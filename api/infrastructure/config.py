import os

from pydantic import BaseModel, Field


class Postgres(BaseModel):
    DSN: str = Field(default="postgres://local:local@db:5432/local")
    MIN_SIZE: int = Field(default=1)
    MAX_SIZE: int = Field(default=100)
    MAX_CONN_ATTEMPT: int = Field(default=5)


class AppConfig(BaseModel):
    postgres_config: Postgres

    @classmethod
    def initialize(cls) -> "AppConfig":
        envs = os.environ
        postgres_config = Postgres(**envs)

        return AppConfig(postgres_config=postgres_config)
