from dishka import make_async_container

from .service import ServiceProvider
from .database import DatabaseProvider
from .application import InteractorProvider


async_container = make_async_container(
    ServiceProvider(),
    DatabaseProvider(),
    InteractorProvider(),
)
