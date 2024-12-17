from dishka import FromDishka as Depends
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter


sub_router = APIRouter(route_class=DishkaRoute)


@sub_router.get("/")
async def get_subscriptions():
    ...
    return 

@sub_router.get("/{id}")
async def get_subscription_by_id(
        id: int
):
    ...
    return 

@sub_router.post("/")
async def create_subscription():
    ...
    return 

@sub_router.put("/")
async def change_subscription():
    ...
    return 

@sub_router.delete("/")
async def delete_subscription():
    ...
    return 
