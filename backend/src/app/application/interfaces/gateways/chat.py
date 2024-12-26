from abc import abstractmethod
from typing import List, Protocol

from app.domain.entities.chat import Chat
from app.domain.entities.message import Message
from app.domain.entities.user_id import UserId
from app.application.dto.chat import CreateChatDTO, MessageDTO


class ChatGateway(Protocol):
    @abstractmethod
    async def add(self, chat: CreateChatDTO) -> int:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, chat_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_chats(self, user_id: UserId) -> List[Chat]:
        raise NotImplementedError

    @abstractmethod
    async def get_chat_owner(self, chat_id: int) -> UserId:
        raise NotImplementedError

    @abstractmethod
    async def get_chat_history(self, chat_id: int) -> List[Message]:
        raise NotImplementedError

    @abstractmethod
    async def save_message(self, message: MessageDTO) -> Message:
        raise NotImplementedError
