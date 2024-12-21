from dishka import FromDishka as Depends
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from app.application.user.get_user import GetUserInteractor
from app.application.dto.user import GetUserDto
from app.domain.entities.user_id import UserId
from app.domain.entities.user import User


admin_router = APIRouter(route_class=DishkaRoute)


@admin_router.get("/users")
async def get_users():
    ...

@admin_router.get("/users/{id}")
async def get_user_by_id(
        get_user: Depends[GetUserInteractor],
        id: UserId
) -> User:
    user = await get_user(GetUserDto(id))
    return user

@admin_router.put("/users/{id}/active_status")
async def change_active_status(
        id: UserId
):
    ...
    return 
