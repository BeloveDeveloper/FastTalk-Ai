from dishka import FromDishka as Depends
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter


user_sub_router = APIRouter(prefix='/sub', route_class=DishkaRoute)


@user_sub_router.get("/")
async def get_my_sub():
    ...
    return


@user_sub_router.post("/purchase")
async def purchase_subscription():
    ...
    return


@user_sub_router.post("/cansel")
async def cancel_subscription():
    ...
    return
