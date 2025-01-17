from typing import List, Any, Optional
import json

from sqlalchemy import Delete, Insert, Update, exists, select, Row
from sqlalchemy.orm import Session
from redis.asyncio import Redis

from app.application.interfaces.gateways.subscription import SubscriptionGateway
from app.domain.entities.subscription import Subscription
from app.infrastructure.database.models import SubscriptionDB
from app.application.dto.subscription import (
    CreateSubscriptionDTO,
    UpdateSubscriptionDTO,
)


class SubcriptionMapper(SubscriptionGateway):

    def __init__(self, session: Session, cache: Redis):
        self.session = session
        self.cache = cache

    def _load(self, row: Row[Any]) -> Subscription:
        return Subscription(
            id=row.id,
            title=row.title,
            description=row.description,
            price=row.price,
            req_limit=row.req_limit,
        )

    async def _clear_cache(self) -> None:
        keys = await self.cache.keys("cache.api.v1.subs:*")
        if keys:
            await self.cache.delete(*keys)
        return

    async def _set_cache(self, subscripistion: Subscription) -> None:
        subscription_json = json.dumps(subscripistion.__dict__)
        await self.cache.setex(
            f"cache.api.v1.subs:{subscripistion.id}", 3600, subscription_json
        )
        return

    async def _get_cache(self, key: str) -> Optional[Subscription]:
        user_json = await self.cache.get(key)
        if user_json:
            user_dict = json.loads(user_json)
            return Subscription(**user_dict)
        return

    async def add(self, subscription: CreateSubscriptionDTO) -> None:
        statement = Insert(SubscriptionDB).values(
            title=subscription.title,
            description=subscription.description,
            price=subscription.price,
            req_limit=subscription.req_limit,
        )
        await self.session.execute(statement)
        await self._clear_cache()
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
        await self._clear_cache()
        return

    async def delete(self, subscription_id: int) -> None:
        statement = Delete(SubscriptionDB).where(SubscriptionDB.id == subscription_id)
        await self.session.execute(statement)
        await self._clear_cache()
        return

    async def check_data_unique(self, title: str) -> bool:
        statement = select(exists().where(SubscriptionDB.title == title))
        result = await self.session.execute(statement)
        return result.scalar_one()

    async def get_subscriptions(self) -> List[Subscription]:

        keys = await self.cache.keys("cache.api.v1.subs:*")
        subscriptions = []
        for key in keys:
            subscription = await self._get_cache(key)
            subscriptions.append(subscription)
        if subscriptions:
            return subscriptions

        statement = select(SubscriptionDB)
        result = await self.session.execute(statement)
        rows = result.fetchall()
        subscriptions = [self._load(row[0]) for row in rows]
        for subscription in subscriptions:
            await self._set_cache(subscription)
        return subscriptions

    async def get_subscription_by_id(self, sub_id: int) -> Subscription:

        subscription = await self._get_cache(f"cache.api.v1.subs:{sub_id}")
        if subscription:
            return subscription

        statement = select(SubscriptionDB).where(SubscriptionDB.id == sub_id)
        result = (await self.session.execute(statement)).one_or_none()
        if result:
            subscription = self._load(result[0])
            await self._set_cache(subscription)
            return subscription
        return
