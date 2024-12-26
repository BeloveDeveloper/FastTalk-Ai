from app.application.interfaces.interactor import Interactor
from app.application.interfaces.uow import UoW
from app.application.interfaces.gateways.subscription import SubscriptionGateway
from app.application.dto.subscription import CreateSubscriptionDTO
from app.domain.exceptions.subscription import SubscriptionAlreadyExistsError


class CreateSubscriptionInteractor(Interactor[CreateSubscriptionDTO, None]):
    def __init__(self, sub_gateway: SubscriptionGateway, uow: UoW) -> None:
        self.sub_gateway = sub_gateway
        self.uow = uow

    async def __call__(self, data: CreateSubscriptionDTO) -> None:
        sub_exist = await self.sub_gateway.check_data_unique(title=data.title)

        if sub_exist:
            raise SubscriptionAlreadyExistsError

        await self.sub_gateway.add(data)
        await self.uow.commit()

        return
