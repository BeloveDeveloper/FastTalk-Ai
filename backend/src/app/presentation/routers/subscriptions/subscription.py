from typing import List
from dishka import FromDishka as Depends
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from app.domain.entities.subscription import Subscription
from app.application.subscription.get_subscriptions import GetSubscriptionsInteractor
from app.application.subscription.get_sub_by_id import GetSubscriptionInteractor
from app.application.subscription.create_subscription import CreateSubscriptionInteractor
from app.application.subscription.update_subscription import UpdateSubscriptionInteractor
from app.application.subscription.delete_subscription import DeleteSubscriptionInteractor
from app.application.dto.subscription import (
    GetSubcriptionDTO,
    CreateSubscriptionDTO, 
    UpdateSubscriptionDTO,
    DeleteSubscriptionDTO
)


sub_router = APIRouter(route_class=DishkaRoute)


@sub_router.get("/")
async def get_subscriptions(
        get_subscriptions: Depends[GetSubscriptionsInteractor]
) -> List[Subscription]:
    subscriptions = await get_subscriptions()
    return subscriptions


@sub_router.get("/{id}")
async def get_subscription_by_id(
        id: int,
        get_subscription: Depends[GetSubscriptionInteractor]
) -> Subscription:
    subscription = await get_subscription(GetSubcriptionDTO(id))
    return subscription


@sub_router.post("/")
async def create_subscription(
        create_sub: Depends[CreateSubscriptionInteractor],
        data: CreateSubscriptionDTO
):
    await create_sub(data)
    return {"message": "Subscription successfully creates"}


@sub_router.put("/")
async def update_subscription(
        update_sub: Depends[UpdateSubscriptionInteractor],
        new_data: UpdateSubscriptionDTO
):
    await update_sub(new_data)
    return {"message": "Subscription successfully updated"}


@sub_router.delete("/{id}")
async def delete_subscription(
        id: int,
        delete_sub: Depends[DeleteSubscriptionInteractor]
):
    await delete_sub(DeleteSubscriptionDTO(id))
    return {"message": f"Subscription with ID {id} deleted"}