from dishka import make_async_container

from .service import ServiceProvider
from .application import ApplicationProvieder
from .infrastructure import InfrastructureProvider


async_container = make_async_container(
    ServiceProvider(),
    ApplicationProvieder(),
    InfrastructureProvider(),
)
