from abc import abstractmethod
from typing import Optional, Protocol

from app.domain.entities.subscription import Subscription
from app.application.dto.subscription import (
    CreateSubscriptionDTO,
    UpdateSubscriptionDTO
)


class SubscriptionGateway(Protocol):
    @abstractmethod
    async def add(self, subscription: CreateSubscriptionDTO) -> None:
        raise NotImplementedError

    @abstractmethod
    async def update(self, subscription: UpdateSubscriptionDTO) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, sub_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    async def check_data_unique(self, title: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def get_subscriptions(self) -> list[Subscription]:
        raise NotImplementedError

    @abstractmethod
    async def get_subscription_by_id(
            self, sub_id: int
    ) -> Optional[Subscription]:
        raise NotImplementedError
