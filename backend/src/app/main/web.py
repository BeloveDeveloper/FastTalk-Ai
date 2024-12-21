from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from .dependencies.ioc import async_container
from .routers import init_routers, register_exception_handlers


def create_app() -> FastAPI:
    app = FastAPI()
    setup_dishka(container=async_container, app=app)
    init_routers(app=app)
    register_exception_handlers(app=app)
    return app


app = create_app()
