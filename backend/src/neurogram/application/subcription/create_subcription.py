from dataclasses import replace

from neurogram.application.interfaces.interactor import Interactor
from neurogram.application.interfaces.uow import UoW
from neurogram.application.interfaces.gateways.subcription import SubcriptionGateway
from neurogram.application.interfaces.hasher import IPasswordHasher
from neurogram.application.dto.subcription import CreateSubcriptionDTO
from neurogram.domain.entities.subscription import Subcription
from neurogram.domain.exceptions.subcription import SubcriptionAlreadyExistsError


class CreateSubcriptionInteractor(Interactor[CreateSubcriptionDTO, None]):
    def __init__(
        self,
        sub_gateway: SubcriptionGateway,
        uow: UoW
    ):
        self.sub_gateway = sub_gateway
        self.uow = uow

    async def __call__(self, data: CreateSubcriptionDTO) -> None:
        sub_exist = await self.sub_gateway.check_data_unique(
            title=data.title
        )

        if sub_exist:
            raise SubcriptionAlreadyExistsError
        
        await self.user_gateway.add(data)
        await self.uow.commit()

        return 