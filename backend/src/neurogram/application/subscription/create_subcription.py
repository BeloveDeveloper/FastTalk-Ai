from neurogram.application.interfaces.interactor import Interactor
from neurogram.application.interfaces.uow import UoW
from neurogram.application.interfaces.gateways.subcription import SubscriptionGateway
from neurogram.application.dto.subcription import CreateSubscriptionDTO
from neurogram.domain.exceptions.subscription import SubscriptionAlreadyExistsError


class CreateSubscriptionInteractor(Interactor[CreateSubscriptionDTO, None]):
    def __init__(
        self,
        sub_gateway: SubscriptionGateway,
        uow: UoW
    ):
        self.sub_gateway = sub_gateway
        self.uow = uow

    async def __call__(self, data: CreateSubscriptionDTO) -> None:
        sub_exist = await self.sub_gateway.check_data_unique(
            title=data.title
        )

        if sub_exist:
            raise SubscriptionAlreadyExistsError
        
        await self.user_gateway.add(data)
        await self.uow.commit()

        return 