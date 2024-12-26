from dataclasses import dataclass
from datetime import datetime


@dataclass
class Chat:
    id: int
    user_id: int
    date: datetime
    title: str
