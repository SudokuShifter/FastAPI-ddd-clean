from dishka import Container, Scope, Provider, provide, make_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from pydantic.v1.typing import convert_generics

from api.domain.example.repositories.example import ExampleRepository
from api.domain.example.services.example import ExampleService
from api.infrastructure.clients.base import BaseClient
from api.infrastructure.database.postgres import PostgresPool
from api.infrastructure.config import AppConfig
from api.infrastructure.interfaces import router
from api.infrastructure.interfaces.router import BaseRouter
from api.presentation.example.router.example import ExampleRouter


class ConfigProvider(Provider):
    @provide(scope=Scope.APP)
    def get_config(self) -> AppConfig:
        return AppConfig.initialize()


class ClientProvider(Provider):
    @provide(scope=Scope.APP)
    def get_base_client(self) -> BaseClient:
        return BaseClient(base_url="yandex.ru")


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def get_postgres(self, config: AppConfig) -> PostgresPool:
        return PostgresPool(config=config.postgres_config)


class RepositoryProvider(Provider):
    @provide(scope=Scope.APP)
    def get_example_repo(self, db: PostgresPool) -> ExampleRepository:
        return ExampleRepository(db=db)


class ServiceProvider(Provider):
    @provide(scope=Scope.APP)
    def get_example_service(
        self, client: BaseClient, repo: ExampleRepository
    ) -> ExampleService:
        return ExampleService(client=client, repo=repo)


class RouterProvider(Provider):
    @provide(scope=Scope.APP)
    def get_example_router(self, service: ExampleService) -> ExampleRouter:
        return ExampleRouter(example_service=service)

    @provide(scope=Scope.APP)
    def get_all_routers(self, example_router: ExampleRouter) -> list[BaseRouter]:
        return [example_router]


def initialize_container() -> Container:
    return make_container(
        ConfigProvider(), ClientProvider(), DatabaseProvider(), RepositoryProvider(), ServiceProvider(), RouterProvider()
    )


def setup_di(container: Container, app: FastAPI):
    return setup_dishka(container=container, app=app)
