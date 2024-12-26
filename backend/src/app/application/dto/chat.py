from dataclasses import dataclass
from app.domain.entities.user_id import UserId


@dataclass
class CreateChatDTO:
    title: str


@dataclass
class DeleteChatDTO:
    chat_id: int


@dataclass
class GetChatHistoryDTO:
    chat_id: int


@dataclass
class MessageDTO:
    text: str
