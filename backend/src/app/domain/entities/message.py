from dataclasses import dataclass
from datetime import datetime


@dataclass
class Message:
    id: int
    chat_id: int
    text: str
    date: datetime
    is_bot: bool
