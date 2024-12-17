from fastapi import FastAPI

from neurogram.presentation.routers.root import root_router
from neurogram.presentation.routers.exc_handler import generic_error_handler, error_map


def init_routers(app: FastAPI) -> None:
    app.include_router(root_router)

def register_exception_handlers(app: FastAPI) -> None:
    for exception_class in error_map.keys():
        app.add_exception_handler(exception_class, generic_error_handler)