from dataclasses import dataclass
from typing import Optional


@dataclass
class CreateUserDTO:
    username: str
    email: Optional[str]
    telegram_id: Optional[int]
    phone_number: Optional[str]
    password: Optional[str]


@dataclass
class GetUserDto:
    id: int