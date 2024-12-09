from dataclasses import dataclass
from typing import Optional

from .user_id import UserId


@dataclass
class User:
    id: UserId
    username: str
    email: Optional[str]
    telegram_id: Optional[int]
    phone_number: Optional[str]
    password: Optional[str]
    total_req: int
    is_premium: bool
    is_active: bool