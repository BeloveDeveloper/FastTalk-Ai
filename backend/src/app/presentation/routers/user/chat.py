from dishka import FromDishka as Depends
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter


user_chat_router = APIRouter(prefix="/chats", route_class=DishkaRoute)


@user_chat_router.get("/")
async def get_chats():
    ...
    return


@user_chat_router.post("/")
async def create_new_chat():
    ...
    return 


@user_chat_router.delete("/")
async def delete_chat():
    ...
    return 


@user_chat_router.get("/{id}/messages")
async def get_messages_by_chat_id(
    id: int
):
    ...
    return 


@user_chat_router.post("/{id}/messages")
async def send_message(
    id: int
):
    ...
    return
