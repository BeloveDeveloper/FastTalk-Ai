from sqlalchemy.orm import Session
from typing import Optional, Any

from sqlalchemy import Update, exists, or_, select, Row
from sqlalchemy.dialects.postgresql import Insert

from neurogram.application.interfaces.gateways.user import UserGateway
from neurogram.domain.entities.user import User
from neurogram.infrastructure.database.models import UserDB
from neurogram.application.dto.user import CreateUserDTO


class SqlUserGateway(UserGateway):

    def __init__(self, session: Session):
        self.session = session

    def _load(self, row: Row[Any]) -> User:
        return User(
            id=row.id,
            username=row.username,
            email=row.email,
            telegram_id=row.telegram_id,
            phone_number=row.phone_number,
            password=row.password_hash,
            total_req=row.total_req,
            is_premium=row.is_premium,
            is_active=row.is_active,
        )
    
    async def add(self, user: CreateUserDTO) -> User:
        statement = (
            Insert(UserDB)
            .values(
                username=user.username,
                email=user.email,
                telegram_id=user.telegram_id,
                phone_number=user.phone_number,
                password_hash=user.password,
            )
            .returning(UserDB.id)
        )
        r = (await self.session.execute(statement)).one()
        print(r)
        return

    async def change_active_status(self, user_id: int, is_active: bool) -> None:
        stmt = (
            Update(UserDB).where(UserDB.id == user_id).values(is_active=is_active)
        )
        await self.session.execute(stmt)
        return

    async def check_data_unique(self, data: CreateUserDTO) -> bool:
        conditions = [UserDB.username == data.username]

        if data.telegram_id:
            conditions.append(UserDB.telegram_id == data.telegram_id)

        if data.email:
            conditions.append(UserDB.email == data.email)

        statement = select(exists().where(or_(*conditions)))
        result = await self.session.execute(statement)
        return result.scalar_one()

    async def get_by_tg_id(self, tg_id: int) -> Optional[User]:
        statement = select(UserDB).where(UserDB.telegram_id == tg_id)
        result = (await self.session.execute(statement)).one_or_none()
        if result:
            return self._load(result[0])
        return 

    async def get_by_id(self, user_id: int) -> Optional[User]:
        statement = select(UserDB).where(UserDB.id == user_id)
        result = (await self.session.execute(statement)).one_or_none()
        if result:
            return self._load(result[0])
        return 
