from datetime import datetime
from app.application.interfaces.gateways.chat import ChatGateway
from sqlalchemy.orm import Session
from typing import List, Any

from sqlalchemy import Delete, Insert, select, Row

from app.infrastructure.database.models import ChatDB, MessageDB
from app.application.dto.chat import CreateChatDTO, MessageDTO
from app.domain.entities.chat import Chat
from app.domain.entities.message import Message
from app.domain.entities.user_id import UserId


class ChatMapper(ChatGateway):
    def __init__(self, session: Session):
        self.session = session

    def _load_chat(self, row: Row[Any]) -> Chat:
        return Chat(
            id=row.id,
            user_id=row.user_id,
            title=row.title,
            date=row.date,
        )

    def _load_message(self, row: Row[Any]) -> Message:
        return Message(
            id=row.id,
            chat_id=row.chat_id,
            text=row.text,
            date=row.date,
            is_bot=row.is_bot,
        )

    async def add(self, chat: CreateChatDTO) -> int:
        date_now = datetime.now()
        statement = (
            Insert(ChatDB)
            .values(
                user_id=chat.user_id,
                date=date_now,
                title=chat.title,
            )
            .returning(ChatDB.id)
        )
        result = await self.session.execute(statement)
        return result.scalar_one()

    async def delete(self, chat_id: int) -> None:
        statement = Delete(ChatDB).where(ChatDB.id == chat_id)
        await self.session.execute(statement)
        return

    async def get_chats(self, user_id: UserId) -> List[Chat]:
        statement = select(ChatDB).where(ChatDB.user_id == user_id)
        result = await self.session.execute(statement)
        rows = result.fetchall()
        chats = [self._load_chat(row[0]) for row in rows]
        return chats

    async def get_chat_owner(self, chat_id: int) -> UserId:
        statement = select(ChatDB.user_id).where(ChatDB.id == chat_id)
        result = await self.session.execute(statement)
        return result.scalar_one()

    async def get_chat_history(self, chat_id: int) -> List[Message]:
        statement = select(MessageDB).where(MessageDB.chat_id == chat_id)
        result = await self.session.execute(statement)
        rows = result.fetchall()
        messages = [self._load_message(row[0]) for row in rows]
        return messages

    async def save_message(self, message: MessageDTO) -> Message:
        date_now = datetime.now()
        statement = (
            Insert(MessageDB)
            .values(
                chat_id=message.chat_id,
                text=message.text,
                date=date_now,
                is_bot=message.is_bot,
            )
            .returning(MessageDB.id)
        )
        result = await self.session.execute(statement)
        message_id = result.scalar_one()

        return Message(
            id=message_id,
            chat_id=message.chat_id,
            text=message.text,
            date=date_now,
            is_bot=message.is_bot,
        )
