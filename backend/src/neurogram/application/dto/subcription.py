from dataclasses import dataclass
from typing import Optional


@dataclass
class CreateSubscriptionDTO:
    title: str
    description: str
    price: int
    limit: int


@dataclass
class UpdateSubscriptionDTO:
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    limit: Optional[int] = None


@dataclass
class DeleteSubscriptionDTO:
    id: int