from abc import abstractmethod
from typing import Optional, Protocol

from neurogram.domain.entities.subscription import Subcription
from neurogram.application.dto.subcription import (
    CreateSubcriptionDTO,
    UpdateSubcriptionDTO
)


class SubcriptionGateway(Protocol):
    @abstractmethod
    async def add(self, subcription: CreateSubcriptionDTO) -> None:
        raise NotImplementedError

    @abstractmethod
    async def update(self, subcription: UpdateSubcriptionDTO) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, sub_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    async def check_data_unique(self, title: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def get_subcriptions(self) -> list[Subcription]:
        raise NotImplementedError
