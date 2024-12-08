from dataclasses import dataclass

from .user_id import UserId


@dataclass
class User:
    id: UserId
    username: str
    email: str
    phone_number: str
    password: str
    total_req: int
    is_premium: bool
    is_active: bool