from api.application import Application
from api.infrastructure.config import AppConfig
from api.infrastructure.dependencies.di import initialize_container
from api.infrastructure.interfaces.router import BaseRouter


def setup():
    container = initialize_container()
    config = container.get(AppConfig)
    routers = container.get(list[BaseRouter])

    return Application(config=config, routers=routers, container=container)
