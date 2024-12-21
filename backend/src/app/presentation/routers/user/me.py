from dishka import FromDishka as Depends
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter


user_router = APIRouter(route_class=DishkaRoute)


@user_router.get("/")
async def get_user_info():
    ...
    return 