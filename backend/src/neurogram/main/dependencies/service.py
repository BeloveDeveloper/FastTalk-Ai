from dishka import Provider, Scope, provide

from neurogram.domain.services.access import AccessService


class ServiceProvider(Provider):
    @provide(scope=Scope.APP)
    def get_acces_service(self) -> AccessService:
        return AccessService()
