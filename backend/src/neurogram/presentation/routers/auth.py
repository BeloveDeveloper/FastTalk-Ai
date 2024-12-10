from dishka import FromDishka as Depends
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from neurogram.application.user.register import RegisterInteractor
from neurogram.application.dto.user import CreateUserDTO

auth_router = APIRouter(route_class=DishkaRoute)


@auth_router.post("/signup")
async def signup(
    register: Depends[RegisterInteractor],
    user: CreateUserDTO,
) -> dict[str, str]:
    await register(user)
    return {"message": "User successfully registered"}