from dishka import Provider, Scope, provide

from neurogram.application.interfaces.uow import UoW
from neurogram.application.user.get_user import GetUserInteractor
from neurogram.application.user.register import RegisterInteractor
from neurogram.application.interfaces.gateways.user import UserGateway
from neurogram.infrastructure.auth.password_hasher import PasswordHasher


class InteractorProvider(Provider):
    @provide(scope=Scope.APP)
    def get_password_hasher(
            self
    ) -> PasswordHasher:
        return PasswordHasher()

    @provide(scope=Scope.REQUEST)
    def get_user_interactor(
            self, 
            user_gateway: UserGateway
    ) -> GetUserInteractor:
        return GetUserInteractor(user_gateway)

    @provide(scope=Scope.REQUEST)
    def get_register_interactor(
            self, 
            user_gateway: UserGateway,
            uow: UoW,
            password_hasher: PasswordHasher
    ) -> RegisterInteractor:
        return RegisterInteractor(
            user_gateway,
            uow,
            password_hasher
        )
