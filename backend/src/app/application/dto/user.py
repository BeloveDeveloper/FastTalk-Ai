from dataclasses import dataclass
from typing import Optional

from app.domain.entities.user_id import UserId


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
    