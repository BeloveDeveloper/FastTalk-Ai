from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from neurogram.main.dependencies.ioc import async_container
from neurogram.presentation.routers.root import root_router



def create_app() -> FastAPI:
    app = FastAPI()
    setup_dishka(container=async_container, app=app)
    app.include_router(root_router)
    return app


app = create_app()
