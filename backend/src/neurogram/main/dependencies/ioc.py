from dishka import make_async_container

from .service import ServiceProvider
from .database import InfrastructureProvider
from .application import ApplicationProvider


provider = make_async_container(
    ServiceProvider(),
    InfrastructureProvider(),
    ApplicationProvider(),
)
