from dishka import FromDishka as Depends
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from app.application.user.get_user import GetUserInteractor
from app.application.dto.user import GetUserDTO
from app.domain.entities.user import User
from app.infrastructure.auth.jwt_auth.jwt_id_provider import TokenIdProvider

user_router = APIRouter(route_class=DishkaRoute)


@user_router.get("/")
async def get_user_info(
    id_provider: Depends[TokenIdProvider],
    get_user: Depends[GetUserInteractor],
) -> User:
    user_id = id_provider.get_current_user_id()
    user = await get_user(GetUserDTO(user_id))
    return user
