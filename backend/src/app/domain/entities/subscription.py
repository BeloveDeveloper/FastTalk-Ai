from dataclasses import dataclass


@dataclass
class Subscription:
    id: int
    title: str
    description: str
    price: int
    req_limit: int
