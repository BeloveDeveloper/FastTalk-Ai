from abc import abstractmethod
from typing import Optional, Protocol

from neurogram.domain.entities.user import User
from neurogram.application.dto.user import CreateUserDTO


class UserGateway(Protocol):
    @abstractmethod
    async def add(self, user: CreateUserDTO) -> User:
        raise NotImplementedError

    @abstractmethod
    async def change_active_status(self, user_id: int, is_active: bool) -> None:
        raise NotImplementedError


    @abstractmethod
    async def check_data_unique(self, user: User) -> bool:
        raise NotImplementedError


    @abstractmethod
    async def get_by_tg_id(self, tg_id: int) -> Optional[User]:
        raise NotImplementedError


    @abstractmethod
    async def get_by_id(self, user_id: int) -> Optional[User]:
        raise NotImplementedError

