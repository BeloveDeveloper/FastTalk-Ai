from typing import List

from app.application.interfaces.interactor import Interactor
from app.application.interfaces.gateways.subscription import SubscriptionGateway
from app.domain.entities.subscription import Subscription


class GetSubscriptionsInteractor(Interactor[None, List[Subscription]]):
    def __init__(
        self,
        sub_gateway: SubscriptionGateway,
    ) -> None:
        self.sub_gateway = sub_gateway

    async def __call__(self) -> List[Subscription]:
        subcriptions = await self.sub_gateway.get_subscriptions()
        return subcriptions
