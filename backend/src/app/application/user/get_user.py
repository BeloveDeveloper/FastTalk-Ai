from app.application.dto.user import GetUserDto
from app.application.interfaces.interactor import Interactor
from app.application.interfaces.gateways.user import UserGateway
from app.domain.entities.user import User
from app.domain.exceptions.user import UserDoesNotExistError


class GetUserInteractor(Interactor[GetUserDto, User]):
    def __init__(self, user_gateway: UserGateway):
        self.user_gateway = user_gateway

    async def __call__(self, data: GetUserDto) -> User:
        user = await self.user_gateway.get_by_id(data.id)
    
        if not user:
            raise UserDoesNotExistError

        return user