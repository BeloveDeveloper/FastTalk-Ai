from dataclasses import dataclass


@dataclass
class Subscription:
    id: int
    title: str
    description: str
    price: int
    limit: int
