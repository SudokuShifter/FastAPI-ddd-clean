from api.domain.example.repositories.example import ExampleRepository
from api.infrastructure.clients.base import BaseClient


class ExampleService:
    def __init__(
        self,
        client: BaseClient,
        repo: ExampleRepository,
    ):
        self.client = client
        self.repo = repo

    async def some_method(self) -> None:
        pass
