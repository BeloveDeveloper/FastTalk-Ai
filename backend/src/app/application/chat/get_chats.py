from typing import List

from app.application.interfaces import id_provider
from app.application.interfaces.gateways.chat import ChatGateway
from app.application.interfaces.id_provider import IdProvider
from app.application.interfaces.interactor import Interactor
from app.domain.entities.chat import Chat


class GetChatsInteractor(Interactor[None, List[Chat]]):
    def __init__(self, chat_gateway: ChatGateway, id_provider: IdProvider) -> None:
        self.chat_gateway = chat_gateway
        self.id_provider = id_provider

    async def __call__(self) -> List[Chat]:
        user_id = self.id_provider.get_current_user_id()
        chats = await self.chat_gateway.get_chats(user_id)
        return chats
