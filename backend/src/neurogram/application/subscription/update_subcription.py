from neurogram.application.interfaces.interactor import Interactor
from neurogram.application.interfaces.uow import UoW
from neurogram.application.interfaces.gateways.subcription import SubcriptionGateway
from neurogram.application.dto.subcription import UpdateSubcriptionDTO
from neurogram.domain.exceptions.subscription import SubcriptionAlreadyExistsError


class UpdateSubcriptionInteractor(Interactor[UpdateSubcriptionDTO, None]):
    def __init__(
        self,
        sub_gateway: SubcriptionGateway,
        uow: UoW
    ):
        self.sub_gateway = sub_gateway
        self.uow = uow

    async def __call__(self, data: UpdateSubcriptionDTO) -> None:
        sub_exist = await self.sub_gateway.check_data_unique(
            title=data.title
        )

        if sub_exist:
            raise SubcriptionAlreadyExistsError
        
        await self.sub_gateway.update(data)
        await self.uow.commit()

        return 