from typing import List

from app.application.dto.chat import GetChatHistoryDTO
from app.application.interfaces.gateways.chat import ChatGateway
from app.application.interfaces.id_provider import IdProvider
from app.application.interfaces.interactor import Interactor
from app.domain.entities.message import Message
from app.domain.services.access import AccessService


class GetChatHistoryInteractor(Interactor[GetChatHistoryDTO, List[Message]]):
    def __init__(
        self,
        chat_gateway: ChatGateway,
        access: AccessService,
        id_provider: IdProvider,
    ) -> None:
        self.chat_gateway = chat_gateway
        self.access = access
        self.id_provider = id_provider

    async def __call__(self, data: GetChatHistoryDTO) -> List[Message]:
        chat_id = data.chat_id
        user_id = self.id_provider.get_current_user_id()
        chat_owner_id = await self.chat_gateway.get_chat_owner(chat_id)
        self.access.ensure_can_chat(user_id, chat_owner_id)

        chat_history = await self.chat_gateway.get_chat_history(chat_id)
        return chat_history
