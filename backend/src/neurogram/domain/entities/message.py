from dataclasses import dataclass


@dataclass
class Message:
    id: int
    chat_id: int
    text: str
    date: str
    is_bot: bool
