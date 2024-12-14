from dishka import FromDishka as Depends
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from neurogram.application.user.get_user import GetUserInteractor
from neurogram.application.dto.user import GetUserDto
from neurogram.domain.entities.user_id import UserId
from neurogram.domain.entities.user import User


admin_router = APIRouter(route_class=DishkaRoute)


@admin_router.get("/")
async def get_users():
    ...
    return 


@admin_router.get("/{id}")
async def get_user_by_id(
        get_user: Depends[GetUserInteractor],
        id: UserId
) -> User:
    user = await get_user(GetUserDto(id))
    return user


@admin_router.put("/{id}/active_status")
async def change_active_status(
        id: UserId
):
    ...
    return 
