from sqlalchemy.orm import Session
from typing import List, Any

from sqlalchemy import Delete, Insert, Update, exists, select, Row

from app.application.interfaces.gateways.subscription import SubscriptionGateway
from app.domain.entities.subscription import Subscription
from app.infrastructure.database.models import SubscriptionDB
from app.application.dto.subscription import (
    CreateSubscriptionDTO,
    UpdateSubscriptionDTO,
)


class SubcriptionMapper(SubscriptionGateway):

    def __init__(self, session: Session):
        self.session = session

    def _load(self, row: Row[Any]) -> Subscription:
        return Subscription(
            id=row.id,
            title=row.title,
            description=row.description,
            price=row.price,
            req_limit=row.req_limit,
        )

    async def add(self, subscription: CreateSubscriptionDTO) -> None:
        statement = Insert(SubscriptionDB).values(
            title=subscription.title,
            description=subscription.description,
            price=subscription.price,
            req_limit=subscription.req_limit,
        )
        await self.session.execute(statement)
        return

    async def update(self, data: UpdateSubscriptionDTO) -> None:
        values_to_update = {
            key: value for key, value in data.__dict__.items() if value is not None
        }

        statement = (
            Update(SubscriptionDB)
            .where(SubscriptionDB.id == data.id)
            .values(**values_to_update)
        )

        await self.session.execute(statement)
        return

    async def delete(self, subscription_id: int) -> None:
        statement = Delete(SubscriptionDB).where(SubscriptionDB.id == subscription_id)
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
        subscriptions = [self._load(row[0]) for row in rows]
        return subscriptions

    async def get_subscription_by_id(self, sub_id: int) -> Subscription:
        statement = select(SubscriptionDB).where(SubscriptionDB.id == sub_id)
        result = (await self.session.execute(statement)).one_or_none()
        if result:
            return self._load(result[0])
        return
