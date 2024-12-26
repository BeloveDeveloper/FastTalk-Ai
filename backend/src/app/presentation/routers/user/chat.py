from typing import List
from app.application.chat.chat_history import GetChatHistoryInteractor
from app.application.chat.create_chat import CreateChatInteractor
from app.application.chat.delete_chat import DeleteChatInteractor
from app.application.chat.get_chats import GetChatsInteractor
from app.application.chat.save_message import SaveMessageInteractor
from app.application.dto.chat import (
    CreateChatDTO,
    DeleteChatDTO,
    GetChatHistoryDTO,
    MessageDTO,
)
from app.domain.entities.chat import Chat
from app.domain.entities.message import Message
from dishka import FromDishka as Depends
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter


user_chat_router = APIRouter(prefix="/chats", route_class=DishkaRoute)


@user_chat_router.get("/")
async def get_user_chats(get_chats: Depends[GetChatsInteractor]) -> List[Chat]:
    chats = await get_chats()
    return chats


@user_chat_router.post("/")
async def create_new_chat(
    create_chat: Depends[CreateChatInteractor], data: CreateChatDTO
):
    chat_id = await create_chat(data)
    return chat_id


@user_chat_router.delete("/")
async def delete_chat(del_chat: Depends[DeleteChatInteractor], data: DeleteChatDTO):
    await del_chat(data)
    return data.chat_id


@user_chat_router.get("/{chat_id}/messages")
async def get_messages_by_chat_id(
    chat_id: int,
    get_chat_history: Depends[GetChatHistoryInteractor],
) -> List[Message]:
    messages = await get_chat_history(GetChatHistoryDTO(chat_id))
    return messages


@user_chat_router.post("/{chat_id}/messages")
async def send_message(
    chat_id: int, save_message: Depends[SaveMessageInteractor], data: MessageDTO
):
    data.chat_id = chat_id
    data.is_bot = False
    message = await save_message(data)
    return message
