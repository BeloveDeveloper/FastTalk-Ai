from dishka import FromDishka as Depends
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Response

from app.infrastructure.auth.jwt_auth.auth import AuthService
from app.application.user.register import RegisterInteractor
from app.application.dto.user import CreateUserDTO, UserLoginDTO

auth_router = APIRouter(route_class=DishkaRoute)


@auth_router.post("/signup")
async def signup(
    register: Depends[RegisterInteractor],
    user: CreateUserDTO,
) -> dict[str, str]:
    await register(user)
    return {"message": "User successfully registered"}


@auth_router.post("/login")
async def login(
    response: Response,
    auth_service: Depends[AuthService],
    user: UserLoginDTO,
) -> dict[str, str]:
    token = await auth_service.authenticate(user)
    response.set_cookie(
        key="access_token", value=token, httponly=True, samesite="strict"
    )
    return {"message": "Successfully login"}


@auth_router.post("/logout")
async def logout(response: Response) -> dict[str, str]:
    response.delete_cookie("access_token", httponly=True)
    return {"message": "Successfully logged out"}
