from app.application.dto.subscription import GetSubcriptionDTO
from app.application.interfaces.interactor import Interactor
from app.application.interfaces.gateways.subscription import SubscriptionGateway
from app.domain.entities.subscription import Subscription
from app.domain.exceptions.subscription import SubscriptionDoesNotExistError


class GetSubscriptionInteractor(Interactor[GetSubcriptionDTO, Subscription]):
    def __init__(self, user_gateway: SubscriptionGateway) -> None:
        self.user_gateway = user_gateway

    async def __call__(self, data: GetSubcriptionDTO) -> Subscription:
        user = await self.user_gateway.get_subscription_by_id(data.id)

        if not user:
            raise SubscriptionDoesNotExistError

        return user
