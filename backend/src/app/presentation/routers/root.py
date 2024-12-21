from fastapi import APIRouter
from dishka.integrations.fastapi import DishkaRoute

from .admin.users import admin_router
from .auth.jwt_auth import auth_router
from .subscriptions.subscription import sub_router
from .user.chat import user_chat_router
from .user.subcription import user_sub_router
from .user.me import user_router


root_router = APIRouter()


root_router.include_router(
    auth_router,
    prefix="/auth",
    tags=["auth"],   
)

root_router.include_router(
    admin_router,
    prefix="/admin",
    tags=["admin"],
)

root_router.include_router(
    user_router,
    prefix="/me",
    tags=["user"],   
)

root_router.include_router(
    user_sub_router,
    prefix="/me",
    tags=["user", "user subcriptions"],
)

root_router.include_router(
    user_chat_router,
    prefix="/me",
    tags=["user", "user chats"],   
)

root_router.include_router(
    sub_router,
    prefix="/sub",
    tags=["subcriptions"],   
)