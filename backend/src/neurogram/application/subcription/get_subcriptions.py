from dataclasses import replace
from neurogram.application.interfaces.interactor import Interactor
from neurogram.application.interfaces.gateways.subcription import SubcriptionGateway
from neurogram.domain.entities.subscription import Subcription


class GetSubcriptionsInteractor(Interactor[None, list[Subcription]]):
    def __init__(
        self,
        sub_gateway: SubcriptionGateway,
    ):
        self.sub_gateway = sub_gateway

    async def __call__(self) -> list[Subcription]:
        subcriptions = await self.sub_gateway.get_subcriptions()
        return subcriptions