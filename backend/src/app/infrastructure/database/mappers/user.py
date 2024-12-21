from sqlalchemy.orm import Session
from typing import Optional, Any

from sqlalchemy import Insert, Update, exists, or_, select, Row

from app.application.interfaces.gateways.user import UserGateway
from app.domain.entities.user import User
from app.infrastructure.database.models import UserDB
from app.application.dto.user import CreateUserDTO


class UserMapper(UserGateway):

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
            sub_id=row.is_premium,
            is_active=row.is_active,
        )
    
    async def add(self, user: CreateUserDTO) -> None:
        statement = (
            Insert(UserDB)
            .values(
                username=user.username,
                email=user.email,
                telegram_id=user.telegram_id,
                phone_number=user.phone_number,
                password_hash=user.password,
            )
        )
        await self.session.execute(statement)
        return 

    async def change_active_status(self, user_id: int, is_active: bool) -> None:
        stmt = (
            Update(UserDB).where(UserDB.id == user_id).values(is_active=is_active)
        )
        await self.session.execute(stmt)
        return

    async def check_data_unique(
            self, username: str, telegram_id: int, email: str
        ) -> bool:
        conditions = [UserDB.username == username]

        if telegram_id:
            conditions.append(UserDB.telegram_id == telegram_id)

        if email:
            conditions.append(UserDB.email == email)

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
