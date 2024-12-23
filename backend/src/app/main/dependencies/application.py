from dishka import Provider, Scope, provide

from app.application.interfaces.uow import UoW
from app.application.subscription.get_subscriptions import GetSubscriptionsInteractor
from app.application.subscription.get_sub_by_id import GetSubscriptionInteractor
from app.application.subscription.create_subscription import (
    CreateSubscriptionInteractor,
)
from app.application.subscription.update_subscription import (
    UpdateSubscriptionInteractor,
)
from app.application.subscription.delete_subscription import (
    DeleteSubscriptionInteractor,
)
from app.application.user.get_user import GetUserInteractor
from app.application.user.register import RegisterInteractor
from app.application.interfaces.gateways.user import UserGateway
from app.application.interfaces.gateways.subscription import SubscriptionGateway
from app.infrastructure.auth.jwt_auth.password_hasher import PasswordHasher


class UserProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_user_interactor(self, user_gateway: UserGateway) -> GetUserInteractor:
        return GetUserInteractor(user_gateway)

    @provide(scope=Scope.REQUEST)
    def get_register_interactor(
        self, user_gateway: UserGateway, uow: UoW, password_hasher: PasswordHasher
    ) -> RegisterInteractor:
        return RegisterInteractor(user_gateway, uow, password_hasher)


class SubscriptionProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_subcriptions_interactor(
        self, sub_gateway: SubscriptionGateway
    ) -> GetSubscriptionsInteractor:
        return GetSubscriptionsInteractor(sub_gateway)

    @provide(scope=Scope.REQUEST)
    def get_subcription_interactor(
        self, sub_gateway: SubscriptionGateway
    ) -> GetSubscriptionInteractor:
        return GetSubscriptionInteractor(sub_gateway)

    @provide(scope=Scope.REQUEST)
    def get_create_sub_interactor(
        self,
        sub_gateway: SubscriptionGateway,
        uow: UoW,
    ) -> CreateSubscriptionInteractor:
        return CreateSubscriptionInteractor(
            sub_gateway,
            uow,
        )

    @provide(scope=Scope.REQUEST)
    def get_update_sub_interactor(
        self,
        sub_gateway: SubscriptionGateway,
        uow: UoW,
    ) -> UpdateSubscriptionInteractor:
        return UpdateSubscriptionInteractor(
            sub_gateway,
            uow,
        )

    @provide(scope=Scope.REQUEST)
    def get_delete_sub_interactor(
        self,
        sub_gateway: SubscriptionGateway,
        uow: UoW,
    ) -> DeleteSubscriptionInteractor:
        return DeleteSubscriptionInteractor(
            sub_gateway,
            uow,
        )


class ApplicationProvieder(
    UserProvider,
    SubscriptionProvider,
): ...
