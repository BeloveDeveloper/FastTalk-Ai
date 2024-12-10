from dishka import FromDishka as Depends
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from neurogram.application.user.get_user import GetUserInteractor
from neurogram.application.dto.user import GetUserDto
from neurogram.domain.entities.user_id import UserId
from neurogram.domain.entities.user import User


user_router = APIRouter(route_class=DishkaRoute)


@user_router.get("/{id}")
async def get_user_by_id(
        get_user: Depends[GetUserInteractor],
        id: UserId
) -> User:
    user = await get_user(GetUserDto(id))
    return user