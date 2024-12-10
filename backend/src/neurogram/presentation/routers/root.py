from fastapi import APIRouter
from dishka.integrations.fastapi import DishkaRoute

from .user import user_router
from .auth import auth_router


root_router = APIRouter()


root_router.include_router(
    user_router,
    prefix="/user",
    tags=["user"],
)

root_router.include_router(
    auth_router,
    prefix="/auth",
    tags=["auth"],   
)