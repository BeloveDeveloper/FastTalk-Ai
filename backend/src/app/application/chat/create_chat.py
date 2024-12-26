from dataclasses import replace
from app.application.interfaces.gateways.chat import ChatGateway
from app.application.interfaces.id_provider import IdProvider
from app.application.interfaces.interactor import Interactor
from app.application.interfaces.uow import UoW
from app.application.interfaces.gateways.subscription import SubscriptionGateway
from app.application.dto.chat import CreateChatDTO
from app.domain.exceptions.subscription import SubscriptionAlreadyExistsError


class CreateChatInteractor(Interactor[CreateChatDTO, int]):
    def __init__(
        self, chat_gateway: ChatGateway, uow: UoW, id_provider: IdProvider
    ) -> None:
        self.chat_gateway = chat_gateway
        self.uow = uow
        self.id_provider = id_provider

    async def __call__(self, data: CreateChatDTO) -> None:
        user_id = self.id_provider.get_current_user_id()
        data.user_id = user_id
        chat_id = await self.chat_gateway.add(data)
        await self.uow.commit()
        return chat_id
