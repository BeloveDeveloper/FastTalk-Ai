from dataclasses import dataclass
from typing import Optional

from neurogram.domain.entities.user_id import UserId


@dataclass
class CreateUserDTO:
    username: str
    email: Optional[str]
    telegram_id: Optional[int]
    phone_number: Optional[str]
    password: Optional[str]


@dataclass
class GetUserDto:
    id: UserId
    