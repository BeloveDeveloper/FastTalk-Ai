from dataclasses import dataclass
from typing import Optional


@dataclass
class CreateSubcriptionDTO:
    title: str
    description: str
    price: int
    limit: int


@dataclass
class UpdateSubcriptionDTO:
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    limit: Optional[int] = None


@dataclass
class DeleteSubcriptionDTO:
    id: int