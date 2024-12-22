from dataclasses import dataclass
from typing import Optional


@dataclass
class GetSubcriptionDTO:
    id: int


@dataclass
class CreateSubscriptionDTO:
    title: str
    description: str
    price: int
    req_limit: int


@dataclass
class UpdateSubscriptionDTO:
    id: int
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    req_limit: Optional[int] = None


@dataclass
class DeleteSubscriptionDTO:
    id: int
