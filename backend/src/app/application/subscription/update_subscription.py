from app.application.interfaces.interactor import Interactor
from app.application.interfaces.uow import UoW
from app.application.interfaces.gateways.subscription import SubscriptionGateway
from app.application.dto.subscription import UpdateSubscriptionDTO


class UpdateSubscriptionInteractor(Interactor[UpdateSubscriptionDTO, None]):
    def __init__(self, sub_gateway: SubscriptionGateway, uow: UoW) -> None:
        self.sub_gateway = sub_gateway
        self.uow = uow

    async def __call__(self, data: UpdateSubscriptionDTO) -> None:
        await self.sub_gateway.update(data)
        await self.uow.commit()

        return
