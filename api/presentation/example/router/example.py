from api.infrastructure.interfaces.router import BaseRouter
from api.domain.example.services.example import ExampleService
from api.general.utils import some_utility
from api.general.enums import RoutersMetainfo

from fastapi import APIRouter


class ExampleRouter(BaseRouter):
    def __init__(
        self,
        example_service: ExampleService,
    ):
        self.example_service = example_service
        self.tags = RoutersMetainfo.DEFAULT_TAGS.value
        self.prefix = RoutersMetainfo.DEFAULT_PREFIX.value

    @property
    def router(self) -> APIRouter:
        router = APIRouter()
        self.initialize(router)

        return router

    def initialize(self, router: APIRouter) -> None:
        @router.get("/ping")
        async def ping() -> str:
            return "pong"

        @router.get("/ready")
        async def ready() -> dict:
            return {"status": some_utility()}
