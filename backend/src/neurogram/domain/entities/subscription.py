from dataclasses import dataclass


@dataclass
class Subcription:
    id: int
    title: str
    description: str
    price: int
    limit: int
