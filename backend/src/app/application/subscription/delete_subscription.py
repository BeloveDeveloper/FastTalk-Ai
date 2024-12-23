from app.application.interfaces.interactor import Interactor
from app.application.interfaces.uow import UoW
from app.application.interfaces.gateways.subscription import SubscriptionGateway
from app.application.dto.subscription import DeleteSubscriptionDTO


class DeleteSubscriptionInteractor(Interactor[DeleteSubscriptionDTO, None]):
    def __init__(self, sub_gateway: SubscriptionGateway, uow: UoW):
        self.sub_gateway = sub_gateway
        self.uow = uow

    async def __call__(self, data: DeleteSubscriptionDTO) -> None:
        await self.sub_gateway.delete(data.id)
        await self.uow.commit()

        return
