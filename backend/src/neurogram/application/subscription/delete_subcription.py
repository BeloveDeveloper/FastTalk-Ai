from neurogram.application.interfaces.interactor import Interactor
from neurogram.application.interfaces.uow import UoW
from neurogram.application.interfaces.gateways.subcription import SubcriptionGateway
from neurogram.application.dto.subcription import DeleteSubcriptionDTO


class DeleteSubcriptionInteractor(Interactor[DeleteSubcriptionDTO, None]):
    def __init__(
        self,
        sub_gateway: SubcriptionGateway,
        uow: UoW
    ):
        self.sub_gateway = sub_gateway
        self.uow = uow

    async def __call__(self, data: DeleteSubcriptionDTO) -> None:
        await self.sub_gateway.delete(data.id)
        await self.uow.commit()

        return 