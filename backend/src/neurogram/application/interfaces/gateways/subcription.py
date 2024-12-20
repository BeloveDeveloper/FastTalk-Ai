from abc import abstractmethod
from typing import Protocol

from neurogram.domain.entities.subscription import Subscription
from neurogram.application.dto.subcription import (
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
    async def get_subcriptions(self) -> list[Subscription]:
        raise NotImplementedError
