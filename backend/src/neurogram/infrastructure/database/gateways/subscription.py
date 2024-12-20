from sqlalchemy.orm import Session
from typing import List, Optional, Any

from sqlalchemy import Delete, Insert ,Update, exists, or_, select, Row

from neurogram.application.interfaces.gateways.subcription import SubscriptionGateway
from neurogram.domain.entities.subscription import Subscription
from neurogram.infrastructure.database.models import SubscriptionDB
from neurogram.application.dto.subcription import (
    CreateSubscriptionDTO,
    UpdateSubscriptionDTO
)


class SubcriptionMapper(SubscriptionGateway):

    def __init__(self, session: Session):
        self.session = session

    def _load(self, row: Row[Any]) -> Subscription:
        return Subscription(
            id=row.id,
            title=row.title,
            description=row.description,
            price=row.pricem,
            limit=row.limit
        )
    
    async def add(self, subscription: CreateSubscriptionDTO) -> None:
        statement = (
            Insert(SubscriptionDB)
            .values(
                title=subscription.title,
                description=subscription.description,
                price=subscription.price,
                limit=subscription.limit,
            )
        )
        await self.session.execute(statement)
        return 

    async def update(self, subscription_id: int, updated_data: UpdateSubscriptionDTO) -> None:
        statement = (
            Update(SubscriptionDB)
            .where(SubscriptionDB.id == subscription_id)
            .values(
                title=updated_data.title,
                description=updated_data.description,
                price=updated_data.price,
                limit=updated_data.limit,
            )
        )
        await self.session.execute(statement)
        return

    async def delete(self, subscription_id: int) -> None:
        statement = (
            Delete(SubscriptionDB)
            .where(SubscriptionDB.id == subscription_id)
        )
        await self.session.execute(statement)
        return

    async def check_data_unique(self, title: str) -> bool:
        statement = select(exists().where(SubscriptionDB.title == title))
        result = await self.session.execute(statement)
        return result.scalar_one()

    async def get_subscriptions(self) -> List[Subscription]:
        statement = select(SubscriptionDB)
        result = await self.session.execute(statement)
        rows = result.fetchall()
        subscriptions = [self._load(row) for row in rows]
        return subscriptions