from neurogram.application.dto.user import GetUserDto
from neurogram.application.interfaces.interactor import Interactor
from neurogram.application.interfaces.gateways.user import UserGateway
from neurogram.domain.entities.user_id import UserId
from neurogram.domain.entities.user import User
from neurogram.domain.exceptions.user import UserDoesNotExistError

# rewrite
class GetUserInteractor(Interactor[UserId, User]):
    def __init__(self, user_gateway: UserGateway):
        self.user_gateway = user_gateway

    async def __call__(self, data: GetUserDto) -> User:
        user = await self.user_gateway.get_by_id(data.id)

        if not user:
            raise UserDoesNotExistError()

        return user